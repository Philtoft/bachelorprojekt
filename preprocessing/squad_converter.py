from enum import Enum
from datasets import load_dataset
import pandas as pd
import json
from pathlib import Path


class SquadVersion(str, Enum):
    """A string enum for specifying a `SQuAD` version."""

    V1 = "v1"
    V2 = "v2"


def convert_and_save_squad(version: SquadVersion, out_path: str):
    """
    Converts `SQuAD` to an aggregated context-questions format and saves it as two json files; train and validation.

    Each entry of the dataset will be transformed to be composed of
    a context and an array of questions related to that particular context.
    """

    train, validation = convert_squad(version)

    _save_dataset(version, train, "train", out_path)
    _save_dataset(version, validation, "validation", out_path)


def convert_squad(version: SquadVersion) -> tuple[dict, dict]:
    """
    Converts `SQuAD` to an aggregated context-questions format and returns a tuple for train and validation.

    Each entry of the dataset will be transformed to be composed of
    a context and an array of questions related to that particular context.
    """

    squad_version = "" if version == SquadVersion.V1 else f"_{version}"

    dataset = load_dataset(f"squad{squad_version}")
    df_train = pd.DataFrame(dataset['train'])
    df_validate = pd.DataFrame(dataset['validation'])

    train = {
        "data": _transform_dataset(df_train)
    }
    validation = {
        "data": _transform_dataset(df_validate)
    }

    return train, validation


def _save_dataset(version: SquadVersion, dataset: dict, suffix: str, out_path: str):
    """Save a dataset in json format at the specified `out_path`."""

    Path(out_path).mkdir(parents=True, exist_ok=True)

    with open(f"{out_path}/squad_{version}_{suffix}.json", "w", encoding="utf-8") as outfile:
        json.dump(dataset, outfile, indent=4)


def _transform_dataset(df: pd.DataFrame) -> dict:
    """
    Takes a `Pandas DataFrame` containing a split `SQuAD 2.0` dataset and transforms duplicate contexts to a single one,
    combining it with a list of its related questions.
    Removes all questions that have no associated answer

    Output example:
    ```
    {
        context: "example context",
        questions: [
            "Example question 1",
            "Example question 2",
        ]
    }
    ```
    """

    # Removes all questions with no answer
    df = df.loc[df['answers'].apply(lambda x: len(x.get('text', '')) > 0)]

    # Makes it only include 'context' and 'question' columns
    df = df[["context", "question"]]

    # apply(list) is used to convert the list of questions into a list of strings instead of a list of lists
    # reset_index() is used to convert the index into a column
    df = df.groupby("context")['question'].apply(list).reset_index()

    # remove '\n' and spaces from the context column
    df['context'] = df['context'].apply(lambda x: x.replace('\n', ' ').strip())

    # Change column name from question to questions
    df.rename(columns={'question': 'questions'}, inplace=True)

    return df.to_dict(orient="records")

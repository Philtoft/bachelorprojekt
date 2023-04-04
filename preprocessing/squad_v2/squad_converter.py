from datasets import load_dataset
import pandas as pd
import json


def convert_and_save_squad_v2():
    """
    Converts `SQuAD V2.0` to an aggregated context-questions format and saves it as two json files; train and validation.

    Each entry of the dataset will be transformed to be composed of
    a context and an array of questions related to that particular context.
    """

    dataset = load_dataset("squad_v2")
    df_train = pd.DataFrame(dataset['train'])
    df_validate = pd.DataFrame(dataset['validation'])

    train = {
        "data": _transform_dataset(df_train)
    }
    validation = {
        "data": _transform_dataset(df_validate)
    }

    _save_dataset(train, "train")
    _save_dataset(validation, "validation")


def _save_dataset(dataset: dict, suffix: str):
    with open(f"data/squad_v2/squad_v2_{suffix}.json", "w", encoding="utf-8") as outfile:
        json.dump(dataset, outfile, indent=4)


def _transform_dataset(df: pd.DataFrame) -> dict:
    """
    Takes a `Pandas DataFrame` containing a split `SQuAD V2.0` dataset and transforms duplicate contexts to a single one,
    combining it with a list of its related questions.
    Removes all questions that have no associated answer

    Output example:\n
    {
        context: "example context",
        questions: [
            "Example question 1",\n
            "Example question 2",\n
        ]
    }
    """

    # Removes all questions with no answer
    df = df.loc[df['answers'].apply(lambda x : len(x.get('text','')) > 0)]

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

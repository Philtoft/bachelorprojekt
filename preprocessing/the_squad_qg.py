import json
from datasets import (
    DownloadManager,
    Version,
    Value,
    GeneratorBasedBuilder,
    BuilderConfig,
    DatasetInfo,
    Features,
    SplitGenerator,
    Split
)

_SET_BASE_URL = "https://huggingface.co/datasets/the-coorporation/the_squad_qg/resolve/main/"
_SET_URLS = {
    "v2": {
        "train":  _SET_BASE_URL + "squad_v2_train.json",
        "validation": _SET_BASE_URL + "squad_v2_validation.json"
    },
    "v1": {
        "train":  _SET_BASE_URL + "squad_v1_train.json",
        "validation": _SET_BASE_URL + "squad_v1_validation.json"
    }
}

_DESCRIPTION = """\
A preprocessed version of the Standford Question Answering Dataset (SQuAD) version 2.0 \
consisting of contexts and questions only.

Duplicate contexts have been removed and corresponding questions have been merged into an array per context.

Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable. \

SQuAD 2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable \
questions written adversarially by crowdworkers to look similar to answerable ones. \
To do well on SQuAD 2.0, systems must not only answer questions when possible, but also \
determine when no answer is supported by the paragraph and abstain from answering.
"""

_CITATION = """\
@article{2018arXiv160605250R,
       author = {{Rajpurkar}, Robin, Jian and {Liang}, Percy},
        title = "{Know What You Don't Know: Unanswerable Questions for SQuAD}",
      journal = {arXiv e-prints},
         year = 2018,
          eid = {arXiv:1806.03822v1},
        pages = {arXiv:1806.03822v1},
archivePrefix = {arXiv},
       eprint = {1806.03822v1},
}
"""


class SquadConfig(BuilderConfig):
    """Builder configuration for `SQuAD V2.0`."""

    def __init__(self, **kwargs):
        super(SquadConfig, self).__init__(**kwargs)


class SquadProcessor(GeneratorBasedBuilder):
    """
    `SQuAD V2.0` preprocessor to transform a modified `SQuAD V2.0` dataset to be used for training a `T5 model`
    to generate multiple questions from a single context.
    """
    
    DEFAULT_CONFIG_NAME = "v2"
    BUILDER_CONFIGS = [
        SquadConfig(
            name="v2",
            version=Version("2.0.0", "Removed unanswerable entries"),
            description="Custom SQuAD 2.0 dataset in plain text"
        ),
        SquadConfig(
            name="v1",
            version=Version("1.0.0", ""),
            description="Custom SQuAD 1.1 dataset in plain text"
        )
    ]

    def _info(self) -> DatasetInfo:
        return DatasetInfo(
            description=_DESCRIPTION,
            features=Features(
                {
                    "context": Value("string"),
                    "questions": Value("string")
                }
            ),
            supervised_keys=None,
            homepage="https://huggingface.co/datasets/the-coorporation/the_squad_qg",
            citation=_CITATION,
            task_templates=[]
        )

    def _split_generators(self, dl_manager: DownloadManager) -> list[SplitGenerator]:
        urls = _SET_URLS["v1"] if self.config.name == "v1" else _SET_URLS["v2"] 
        files = dl_manager.download_and_extract(urls)
        
        return [
            SplitGenerator(name=Split.TRAIN, gen_kwargs={"filepath": files["train"]}),
            SplitGenerator(name=Split.VALIDATION, gen_kwargs={"filepath": files["validation"]})
        ]

    def _generate_examples(self, filepath: str):
        key = 0
        with open(filepath, encoding="utf-8") as file:
            squad: dict[str, str] = json.load(file)

            for entry in squad["data"]:
                questions = [question.strip() for question in entry['questions']]
                target_text = " {sep_token} ".join(questions)
                target_text = f"{target_text} {{sep_token}}"
                
                yield key, {
                    "context": entry['context'].strip(),
                    "questions": target_text
                }
                key += 1

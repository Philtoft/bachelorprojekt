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

_SET_BASE_URL = "https://huggingface.co/datasets/the-coorporation/the_squad_v2/resolve/main/"
_SET_URLS = {
    "train":  _SET_BASE_URL + "squad_v2_train.json",
    "validation": _SET_BASE_URL + "squad_v2_validation.json"
}

_DESCRIPTION = """\
Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable. \

SQuAD2.0 combines the 100,000 questions in SQuAD1.1 with over 50,000 unanswerable \
questions written adversarially by crowdworkers to look similar to answerable ones. \
To do well on SQuAD2.0, systems must not only answer questions when possible, but also \
determine when no answer is supported by the paragraph and abstain from answering.
"""

_CITATION = """\
@article{2016arXiv160605250R,
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


class SquadV2Config(BuilderConfig):
    """Builder configuration for `SQuAD V2.0`."""

    def __init__(self, **kwargs):
        super(SquadV2Config, self).__init__(**kwargs)

class SquadV2Processor(GeneratorBasedBuilder):
    """
    `SQuAD V2.0` preprocessor to transform a modified `SQuAD V2.0` dataset to be used for training a `T5 model`
    to generate multiple questions from a single context.
    """

    BUILDER_CONFIGS = [
        SquadV2Config(
            name="plain_text",
            version=Version("1.0.0", ""),
            description="Plain text"
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
            homepage="https://rajpurkar.github.io/SQuAD-explorer/",
            citation=_CITATION,
            task_templates=[]
        )

    def _split_generators(self, dl_manager: DownloadManager) -> list[SplitGenerator]:
        files = dl_manager.download_and_extract(_SET_URLS)

        return [
            SplitGenerator(name=Split.TRAIN, gen_kwargs={"filepath": files["train"]}),
            SplitGenerator(name=Split.VALIDATION, gen_kwargs={"filepath": files["validation"]})
        ]
    
    def _generate_examples(self, filepath: str):
        key = 0
        with open(filepath, encoding="utf-8") as file:
            squad = json.load(file)
            for entry in squad["data"]:
                source_text = f"generate questions: {entry['context'].strip()}"
                questions = [question.strip() for question in entry['questions']]
                target_text = " {sep_token} ".join(questions)
                target_text = f"{target_text} {{sep_token}}"
                yield key, {
                    "context": source_text,
                    "questions": target_text
                }
                key += 1
    
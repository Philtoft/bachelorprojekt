import json
from datasets import (
    builder, 
    DownloadManager, 
    splits, 
    Version,
    info,
    features,
    Value
)

_SET_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
_SET_URLS = {
    "train": _SET_URL + "train-v1.1.json",
    "dev": _SET_URL + "dev-v1.1.json"
}

_DESCRIPTION = """\
Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable.
"""

_CITATION = """\
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
"""


class SquadConfig(builder.BuilderConfig):
    """Builder configuration for SQuAD"""

    def __init__(self, **kwargs):
        super(SquadConfig, self).__init__(**kwargs)


class SquadProcessor(builder.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        SquadConfig(
            name="plain_text",
            version=Version("1.0.0", ""),
            description="Plain text"
        )
    ]

    def _split_generators(self, dl_manager: DownloadManager):
        """Downloads the specified datasets and splits it in trainining and validation sets"""

        files = dl_manager.download_and_extract(_SET_URLS)

        return [
            splits.SplitGenerator(name=splits.Split.TRAIN, gen_kwargs={"filepath": files["train"]}),
            splits.SplitGenerator(name=splits.Split.VALIDATION, gen_kwargs={"filepath": files["dev"]})
        ]

    def _generate_examples(self, filepath):
        # Generates the examples in raw text form, adding the generate question task to each entry.
        # All questions are transformed to a single string, with each being separated by a {sep_token} placeholder.
        
        key = 0
        with open(filepath, encoding="utf-8") as file:
            squad = json.load(file)
            for article in squad["data"]:
                for paragraph in article["paragraphs"]:
                    source_text = f"generate questions: {paragraph['context'].strip()}"
                    questions = [qas['question'].strip() for qas in paragraph['qas']]
                    target_text = " {sep_token} ".join(questions)
                    target_text = f"{target_text} {{sep_token}}"
                    yield key, {
                          "context": source_text,
                          "questions": target_text}
                    key += 1

    def _info(self) -> info.DatasetInfo:
        return info.DatasetInfo(
            description=_DESCRIPTION,
            features=features.Features(
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

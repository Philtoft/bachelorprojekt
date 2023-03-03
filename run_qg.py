from dataclasses import dataclass, field
from transformers import HfArgumentParser, TrainingArguments, T5Tokenizer, BartTokenizer
from typing import Tuple

MODEL_TYPE_TO_TOKENIZER = {
    "t5": T5Tokenizer,
    "bart": BartTokenizer,
}

@dataclass
class ModelArguments:
    model_name: str = field(
        metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )

    model_type: str = field(
        metadata={"help": "t5 or bart"}
    )

@dataclass
class DataTrainingArguments:
    training_file_path: str = field(
        metadata={"help": "Path for cached training dataset"}
    )

    validation_file_path: str = field(
        metadata={"help": "Path for cached validation dataset"}
    )


def main():
    with open("settings.json", "r") as file:
        print(file.read())
    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
    model_args, data_args, training_args = parser.parse_json_file(json_file="./settings.json")

    model_args.model_type = model_args.model_type.lower()

if __name__ == "__main__":
    main()
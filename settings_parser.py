from dataclasses import dataclass, field
from transformers import TrainingArguments, HfArgumentParser
import json

_SETTINGS = "settings.json"

@dataclass
class ModelArguments:
    model_name: str = field(
        metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )


@dataclass
class DataTrainingArguments:
    training_file_path: str = field(
        metadata={"help": "Path for cached training dataset"}
    )

    validation_file_path: str = field(
        metadata={"help": "Path for cached validation dataset"}
    )


def parse_settings(settings_path: str = _SETTINGS) -> tuple[ModelArguments, DataTrainingArguments, TrainingArguments]:
    """Parses the model, data and training arguments for the given model specified in 'settings.json'."""

    with open(settings_path, "r", encoding="utf-8") as file:
        settings = json.load(file)
        mergedEntries = settings['model_arguments'] | settings['data_training_arguments'] | settings['training_arguments']

        parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
        return parser.parse_dict(mergedEntries)

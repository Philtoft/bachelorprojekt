from transformers import TrainingArguments, HfArgumentParser
from parsing.arguments import ModelArguments, DataTrainingArguments
import json


def parse_settings(settings_path: str) -> tuple[ModelArguments, DataTrainingArguments, TrainingArguments]:
    """Parses the model, data and training arguments for the given model specified in 'settings.json'."""

    with open(settings_path, "r", encoding="utf-8") as file:
        settings = json.load(file)

        # Merge dictionaries to one
        mergedEntries = settings['model_arguments'] | settings['data_training_arguments'] | settings['training_arguments']

        parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
        return parser.parse_dict(mergedEntries)

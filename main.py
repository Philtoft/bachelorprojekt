import argparse
import json
import os
import torch
import logging
from arguments import ModelArguments, DataTrainingArguments
from transformers import (
    HfArgumentParser,
    TrainingArguments,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer
)
from training.trainer import QGARTrainer
from preprocessing.preprocessor import Preprocessor
from huggingface_hub import login
from models.qg import QG


_SETTINGS = "./settings.json"
_TOKEN_PATH = ".local/hg_token.txt"

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace):
    # Log into Huggingface Hub
    login(get_hg_token(), add_to_git_credential=True)

    # Parse settings.json
    model_args, data_args, training_args = parse_settings()
    device = "cuda" if torch.cuda.is_available() else "cpu"

    if args.train:
        logger.warning("--- Training ---")
        train_model(model_args.model_name, device, data_args, training_args)
        exit()
    elif args.input:
        logger.warning("--- Question Generation ---")
        qg = QG()
        print(json.dumps(qg(args.input), indent=4))
        exit()
    else:
        parser.print_help()


def train_model(model_name: str, device: str, data_args: DataTrainingArguments, training_args: TrainingArguments):
    """
    Trains the specified model on the provided datasets using the specified training arguments.
    If the datasets are not present locally, they will be redownloaded and preprocesed.
    """
    model, tokenizer = load_model_and_tokenizer(model_name, device)

    # Check if datasets are available
    if (not os.path.exists(data_args.training_file_path) or not os.path.exists(data_args.validation_file_path)):
        logger.warning("Datasets not present in './data/'.")
        create_datasets(model, tokenizer)

    # Initialize trainer
    trainer = QGARTrainer(
        model,
        tokenizer,
        data_args.training_file_path,
        data_args.training_file_path,
        training_args
    )

    trainer.train()


def create_datasets(model, tokenizer):
    """Downloads and preprocesses the SQuAD dataset for model training."""

    preprocessor = Preprocessor(model, tokenizer)
    preprocessor.preprocess_dataset()


def get_hg_token() -> str:
    with open(_TOKEN_PATH, "r") as file:
        return file.read()


def load_model_and_tokenizer(model_name: str, device: str) -> tuple[PreTrainedModel, PreTrainedTokenizer]:
    # Load model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
    tokenizer = AutoTokenizer.from_pretrained("t5-small", model_max_length=512)

    tokenizer.sep_token = '<sep>'
    tokenizer.add_tokens(['<sep>'])
    model.resize_token_embeddings(len(tokenizer))

    return model, tokenizer


def parse_settings() -> tuple[ModelArguments, DataTrainingArguments, TrainingArguments]:
    """Parses the model, data and training arguments for the given model specified in 'settings.json'."""

    with open(_SETTINGS, "r", encoding="utf-8") as file:
        settings = json.load(file)
        mergedEntries = settings['model_arguments'] | settings['data_training_arguments'] | settings['training_arguments']

        parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
        return parser.parse_dict(mergedEntries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='QGAR', description="Run or train the QGAR model.")
    parser.add_argument("-t", "--train", action='store_true', help="Specify that the model should be trained.")
    parser.add_argument("-i", "--input", type=str, metavar="text", help="Input text to the model.")

    main(parser.parse_args())

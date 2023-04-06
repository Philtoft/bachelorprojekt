import argparse
import sys
import logging
import json
from huggingface_hub import login
from parsing.settings_parser import parse_settings
from models.qg import QG
from preprocessing.squad_preprocessor import SquadPreprocessor


_HF_TOKEN = "hg_token.txt"
_WANDB_TOKEN = "wandb_token.txt"

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace, no_arguments: bool):
    # Log into Huggingface Hub
    hf_token = get_local_file(_HF_TOKEN)
    login(hf_token, add_to_git_credential=True)

    # Parse settings.json
    model_args, data_args, training_args = parse_settings()
    
    if no_arguments:
        parser.print_help()
    else:
        qg = QG(model_args.qg_model_name, model_args.tokenizer_name)

        if args.input:
            logger.info("--- Question Generation ---")
            qg_result = qg(args.input)
            print(json.dumps(qg_result, indent=4))

        elif args.train:
            logger.info("--- Training ---")
            wandb_token = get_local_file(_WANDB_TOKEN)
            qg.train(training_args, data_args, wandb_token)

        elif args.dataset:
            logger.info("--- Dataset ---")
            p = SquadPreprocessor(qg._tokenizer)
            p.preprocess(data_args.dataset, data_args.dataset_output_dir)

        else:
            print("Unknown command")


def get_local_file(filename: str):
    """Load and return the content of a `.local` file."""

    with open(f'.local/{filename}', 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='QG', description="Run or train the QG model.")
    parser.add_argument("-t", "--train", action='store_true', help="Specify that the model should be trained.")
    parser.add_argument("-d", "--dataset", action='store_true', help="Download and preprocess SQuAD dataset.")
    parser.add_argument("-i", "--input", type=str, metavar="text", help="Input text to the model.")

    main(parser.parse_args(), not (len(sys.argv) > 1))

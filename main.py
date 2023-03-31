import argparse
import sys
import logging
import json
from huggingface_hub import login
from parsing.settings_parser import parse_settings
from models.qg import QG
from preprocessing.preprocessor import SquadPreprocessor


_HF_TOKEN_PATH = ".local/hg_token.txt"
_WANDB_TOKEN_PATH = ".local/wandb_token.txt"

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace, no_arguments: bool):
    # Log into Huggingface Hub
    log_into_hf_hub()

    # Parse settings.json
    _, data_args, training_args = parse_settings()
    
    if no_arguments:
        parser.print_help()
    else:
        qg = QG("t5-small", "t5-small")

        if args.input:
            logger.warning("--- Question Generation ---")
            print(json.dumps(qg(args.input), indent=4))
        elif args.train:
            logger.warning("--- Training ---")
            qg.train(training_args, data_args, get_wandb_token())
        elif args.dataset:
            logger.warning("--- Dataset ---")
            p = SquadPreprocessor(qg._model, qg._tokenizer)
            p.preprocess_dataset()
        else:
            print("Unknown command")


def log_into_hf_hub(token_path: str = _HF_TOKEN_PATH):
    """Logs into the Huggin Face hub using the provided access token."""

    with open(token_path, "r") as file:
        login(file.read(), add_to_git_credential=True)

def get_wandb_token(token_path: str = _WANDB_TOKEN_PATH) -> str:
    """Loads and returns the wandb access token from the given path."""

    with open(token_path, "r") as file:
        return file.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='QG', description="Run or train the QG model.")
    parser.add_argument("-t", "--train", action='store_true', help="Specify that the model should be trained.")
    parser.add_argument("-d", "--dataset", action='store_true', help="Download and preprocess SQuAD dataset.")
    parser.add_argument("-i", "--input", type=str, metavar="text", help="Input text to the model.")

    main(parser.parse_args(), not (len(sys.argv) > 1))

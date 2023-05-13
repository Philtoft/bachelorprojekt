import argparse
import sys
import logging
import json
from huggingface_hub import login
from parsing.settings_parser import parse_settings
from models.qg import QG
from models.qgar import QGAR
from preprocessing.squad_preprocessor import SquadPreprocessor


_HF_TOKEN = "hg_token.txt"
_WANDB_TOKEN = "wandb_token.txt"
_DEFAULT_SETTINGS = "settings.json"

logger = logging.getLogger(__name__)


def main(args: argparse.Namespace, no_arguments: bool):
    if no_arguments:
        print("No arguments provided.")
        parser.print_help()
    else:
        # Log into Huggingface Hub
        hf_token = get_local_file(_HF_TOKEN)
        login(hf_token, add_to_git_credential=True)

        # Parse settings file
        model_args, data_args, training_args = parse_settings(args.settings)
        
        qg = QG(model_args.qg_model_name, model_args.tokenizer_name)
        qgar = QGAR(qg, model_args.qa_model_name)

        if args.dataset:
            logger.info("--- Preprocess Dataset ---")
            preprocessor = SquadPreprocessor(qg._tokenizer)
            preprocessor.preprocess_and_save(data_args.dataset, data_args.dataset_output_dir)

        if args.train:
            logger.info("--- QG Training ---")
            wandb_token = get_local_file(_WANDB_TOKEN)
            qg.train(training_args, data_args, wandb_token)

        if args.note:
            logger.info("--- QGAR ---")
            qgar(args.note, args.out)

        if args.evaluate:
            logger.info("--- EVALUATE QG ---")
            qg.evaluate()

        elif args.qg:
            logger.info("--- Question Generation ---")
            qg_result = qg(args.qg)
            print(json.dumps(qg_result, indent=4))


def get_local_file(filename: str):
    """Load and return the content of a `.local` file."""

    with open(f'.local/{filename}', 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main', description="Run or train the QGAR model.")
    parser.add_argument("-t", "--train", action='store_true', help="Specify that the QG model should be trained.")
    parser.add_argument("-d", "--dataset", action='store_true', help="Download and preprocess SQuAD dataset.")
    parser.add_argument("-qg", "--qg", type=str, metavar="context", help="Create questions based on the input text.")
    parser.add_argument("-s", "--settings", type=str, metavar="settings", default=_DEFAULT_SETTINGS, help="Settings file to use.")
    parser.add_argument("-n", "--note", type=str, metavar="note_path", help="Path to note.")
    parser.add_argument("-e", "--evaluate", action='store_true', help="Whether to evaluate the model or not.")
    parser.add_argument("-o", "--out", type=str, metavar='out_format', default='csv', help="Whether to output to CSV or JSON.")

    main(parser.parse_args(), not (len(sys.argv) > 1))

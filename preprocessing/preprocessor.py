from datasets import load_dataset, DownloadMode
from transformers import PreTrainedModel, PreTrainedTokenizer
import torch
import logging

_MAX_INPUT_LENGTH = 512
_MAX_TARGET_LENGTH = 64
_EOS_TOKEN = ' </s>'
_SEP_TOKEN = '<sep>'
_SQUAD_PROCESSOR_PATH = "preprocessing/squad_v2/squad_v2_processor.py"

logger = logging.getLogger(__name__)


class SquadPreprocessor:
    """
    A `SQuAD` preprocessor for a modified version of `SQuAD 2.0`.

    The preprocessor preprocesses the dataset by adding special tokens and 
    encodings to all of the dataset's entries.
    """

    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer):
        """Initializes a new instance of a `SquadPreprocessor`."""

        self._model = model
        self._tokenizer = tokenizer


    def preprocess_dataset(self, loader_script: str = _SQUAD_PROCESSOR_PATH):
        """
        Preprocesses a modified `SQuAD V2.0` dataset by adding end of sequence and separator tokens 
        to each dataset entry followed by an encoding of the entry.

        The preprocessed dataset is saved in `PyTorch` format locally on disk.
        """

        logger.warning("Downloading SQuAD V2.0 dataset...")
        raw_dataset = load_dataset(loader_script, download_mode=DownloadMode.FORCE_REDOWNLOAD)
        logger.warning("Download complete.")

        # Each question is separated with a <sep> token.
        # Therefore we must add it to the tokenizer's tokens
        self._tokenizer.sep_token = '<sep>'
        self._tokenizer.add_tokens(['<sep>'])
        self._model.resize_token_embeddings(len(self._tokenizer))

        # For each dataset entry point, add eos, <sep>, and encodings
        logger.warning("Preprocessing SQuAD dataset (1/3)")
        logger.warning("Adding eos tokens...")
        tokenized_dataset = raw_dataset.map(self._add_eos_tokens)
        logger.warning("Preprocessing SQuAD dataset (2/3)")
        logger.warning("Adding sep tokens...")
        tokenized_dataset = tokenized_dataset.map(self._add_sep_tokens)
        logger.warning("Preprocessing SQuAD dataset (3/3)")
        logger.warning("Creating encodings...")
        tokenized_dataset = tokenized_dataset.map(self._create_encodings, batched=True)
        logger.warning("Done.")

        # Remove columns 'context' and 'questions'
        tokenized_dataset = tokenized_dataset.remove_columns(["context", "questions"])

        # Split dataset in training and validation
        training_dataset = tokenized_dataset["train"]
        validation_dataset = tokenized_dataset["validation"]

        # Add encoding columns to the split dataset
        columns = ['input_ids', 'attention_mask', 'decoder_input_ids', 'decoder_attention_mask']
        training_dataset.set_format(type='torch', columns=columns)
        validation_dataset.set_format(type='torch', columns=columns)

        # Save split dataset to disk in PyTorch format
        logger.warning("Saving processed dataset to directory 'data/'...")
        torch.save(training_dataset, 'data/training_data.pt')
        torch.save(validation_dataset, 'data/validation_data.pt')
        logger.warning("Successfully saved processed datasets.")

        return tokenized_dataset


    def _create_encodings(self, example_batch) -> dict:
        """
        Creates encodings for each example batch and returns them as a dict.
        """

        # Encode inputs (context)
        input_encoding = self._tokenizer.batch_encode_plus(
            example_batch['context'],
            max_length=_MAX_INPUT_LENGTH,
            add_special_tokens=True,
            truncation=True,
            padding='max_length'
        )

        # Encode targets (all questions for the given context)
        target_encoding = self._tokenizer.batch_encode_plus(
            example_batch['questions'],
            max_length=_MAX_TARGET_LENGTH,
            add_special_tokens=True,
            truncation=True,
            padding='max_length'
        )

        encoding = {
            'input_ids': input_encoding['input_ids'],
            'attention_mask': input_encoding['attention_mask'],
            'decoder_input_ids': target_encoding['input_ids'],
            'decoder_attention_mask': target_encoding['attention_mask']
        }

        return encoding


    def _add_eos_tokens(self, example):
        """Adds an `end of sequence (eos)` token to an example's context and questions."""

        example['context'] = example['context'] + _EOS_TOKEN
        example['questions'] = example['questions'] + _EOS_TOKEN
        return example


    def _add_sep_tokens(self, example):
        """Replaces the `{sep_token}` placeholder with a `<sep>` token for an example's questions."""

        example['questions'] = example['questions'].replace("{sep_token}", _SEP_TOKEN)
        return example

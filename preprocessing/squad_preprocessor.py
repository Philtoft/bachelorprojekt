from transformers import T5TokenizerFast, BatchEncoding
from datasets import DownloadMode, Dataset, load_dataset
import torch
import logging

_TASK_PREFIX = "generate questions: "
_SEP_TOKEN = '<sep>'
_EOS_TOKEN = ' </s>'
_MAX_INPUT_OUTPUT_LENGTH = 512

logger = logging.getLogger(__name__)


class SquadPreprocessor:
    """
    A `SQuAD` preprocessor for a modified version of the `SQuAD` dataset.
    
    The preprocessor preprocesses the dataset by adding special tokens and 
    encodings to all entries in the dataset.
    """

    def __init__(self, tokenizer: T5TokenizerFast, padding: bool = False):
        """
        Initializes a new instance of a `SquadPreprocessor`.

        `padding` specifies whether to pad the entries in the dataset to the longest entry of the entire dataset.
        """

        self._tokenizer = tokenizer
        self._padding = padding

        # Each question is separated with a <sep> token.
        # Therefore we must add it to the tokenizer's tokens
        self._tokenizer.sep_token = _SEP_TOKEN
        self._tokenizer.add_tokens([_SEP_TOKEN])


    def preprocess_and_save(self, dataset: str, save_dir: str):
        """
        Preprocesses a modified `SQuAD` dataset by adding end of sequence and separator tokens 
        to each dataset entry followed by an encoding of the entry.

        The preprocessed dataset is saved in `PyTorch` format locally on disk in `save_dir`.
        """

        train, validation = self.preprocess(dataset)

        # Save datasets to disk if save_dir is specified
        logger.info(f"Saving processed dataset to {save_dir}")
        torch.save(train, save_dir + "/training_data.pt")
        torch.save(validation, save_dir + "/validation_data.pt")
        logger.info("Successfully saved processed datasets.")


    def preprocess(self, dataset: str) -> tuple[Dataset, Dataset]:
        """
        Preprocesses a modified `SQuAD` dataset by adding end of sequence and separator tokens 
        to each dataset entry followed by an encoding of the entry.

        Returns the in memory preprocessed train and validaiton datasets.
        """

        logger.info(f"Downloading '{dataset}' dataset...")
        raw_dataset = load_dataset(dataset, download_mode=DownloadMode.FORCE_REDOWNLOAD)
        logger.info("Download complete.")

        logger.info("Preprocessing (1/3)")
        logger.info("Adding eos tokens...")
        tokenized_dataset = raw_dataset.map(self._add_eos_tokens)

        logger.info("Preprocessing (2/3)")
        logger.info("Adding sep tokens...")
        tokenized_dataset = tokenized_dataset.map(self._add_sep_tokens)

        logger.info("Preprocessing (3/3)")
        logger.info("Creating encodings...")
        tokenized_dataset = tokenized_dataset.map(self._create_encodings, batched=True)
        logger.info("Done.")

        # Remove redundant columns 'context' and 'questions' from the tokenized dataset
        tokenized_dataset = tokenized_dataset.remove_columns(['context', 'questions'])

        # Split dataset in training and validation
        training_dataset = tokenized_dataset["train"]
        validation_dataset = tokenized_dataset["validation"]

        return training_dataset, validation_dataset


    def _create_encodings(self, batch: dict) -> BatchEncoding:
        """
        Creates encodings for each example batch and returns them as a `BatchEncoding`.
        """

        # Add task prefix to each context
        inputs = [_TASK_PREFIX + context for context in batch['context']]

        # Encode inputs (context)
        input_encodings = self._tokenizer(
            inputs,
            max_length=_MAX_INPUT_OUTPUT_LENGTH,
            add_special_tokens=True,
            truncation=True,
            padding=self._padding if not self._padding else 'max_length'
        )

        # Encode targets (all questions for the given context)
        labels = self._tokenizer(
            batch['questions'],
            max_length=_MAX_INPUT_OUTPUT_LENGTH,
            add_special_tokens=True,
            truncation=True,
            padding=self._padding if not self._padding else 'max_length'
        )

        # Note: The forward function automatically creates the correct decoder_input_ids
        # Hence, we don't create them manually
        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': labels['input_ids']
        }


    def _add_eos_tokens(self, example: dict[str, str]):
        """Adds an `end of sequence (eos)` token to an example's context and questions."""

        example['context'] = example['context'] + _EOS_TOKEN
        example['questions'] = example['questions'] + _EOS_TOKEN

        return example


    def _add_sep_tokens(self, example: dict[str, str]):
        """Replaces the `{sep_token}` placeholder with a `<sep>` token for an example's questions."""

        example['questions'] = example['questions'].replace('{sep_token}', _SEP_TOKEN)

        return example

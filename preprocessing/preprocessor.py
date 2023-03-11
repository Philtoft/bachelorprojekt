from datasets import load_dataset
import torch
import logging

_MAX_INPUT_LENGTH = 512
_MAX_TARGET_LENGTH = 64
_EOS_TOKEN = "</s>"
_SEP_TOKEN = "<sep>"

logger = logging.getLogger(__name__)

class Preprocessor:
    def __init__(self, model, tokenizer):
        self._model = model
        self._tokenizer = tokenizer
        
    def preprocess_dataset(self):
        logger.warning("Downloading SQuAD dataset...")
        raw_dataset = load_dataset("./preprocessing/squad_processor.py")
        logger.warning("Download complete.")
        
        # Each question is separated with a <sep> token. 
        # Therefore we need to add it to the tokenizer tokens
        self._tokenizer.sep_token = '<sep>'
        self._tokenizer.add_tokens(['<sep>'])
        self._model.resize_token_embeddings(len(self._tokenizer))

        # For each dataset entry point add eos, <sep>, and encodings
        logger.warning("Preprocessing SQuAD dataset...")
        tokenized_dataset = raw_dataset.map(self._add_eos_tokens)
        tokenized_dataset = tokenized_dataset.map(self._add_sep_tokens)
        tokenized_dataset = tokenized_dataset.map(self._create_encodings, batched=True)
        logger.warning("Done.")
        
        # Remove columns 'context' and 'questions'
        tokenized_dataset = tokenized_dataset.remove_columns(["context", "questions"])

        # Split dataset in training and validation
        training_dataset = tokenized_dataset["train"]
        validation_dataset = tokenized_dataset["validation"]

        # Add encoding columns to the split dataset
        columns = ['input_ids', 'decoder_input_ids', 'attention_mask', 'decoder_attention_mask']
        training_dataset.set_format(type='torch', columns=columns)
        validation_dataset.set_format(type='torch', columns=columns)

        # Save split dataset to disk in PyTorch format
        logger.warning("Saving processed dataset to directory './data/'...")
        torch.save(training_dataset, './data/training_data.pt')
        torch.save(validation_dataset, './data/validation_data.pt')
        logger.warning("Successfully saved processed datasets.")

    def _create_encodings(self, example_batch):
        input_encodings = self._tokenizer.batch_encode_plus(
            example_batch['context'], 
            max_length=_MAX_INPUT_LENGTH, 
            add_special_tokens=True,
            truncation=True, 
            padding='max_length'
        )
        
        target_encodings = self._tokenizer.batch_encode_plus(
            example_batch['questions'], 
            max_length=_MAX_TARGET_LENGTH, 
            add_special_tokens=True,
            truncation=True, 
            padding='max_length'
        )

        encodings = {
            'input_ids': input_encodings['input_ids'], 
            'attention_mask': input_encodings['attention_mask'],
            'decoder_input_ids': target_encodings['input_ids'],
            'decoder_attention_mask': target_encodings['attention_mask']
        }

        return encodings

    def _add_eos_tokens(self, example):
        """Adds an end of sequence (eos) token to a training example's context and questions."""
        
        example['context'] = example['context'] + " " + _EOS_TOKEN
        example['questions'] = example['questions'] + " " + _EOS_TOKEN
        return example

    def _add_sep_tokens(self, example):
        """Replaces the {sep_token} placeholder with <sep> for a training example's questions."""

        example['questions'] = example['questions'].replace("{sep_token}", _SEP_TOKEN)
        return example
from typing import Any
from transformers import Trainer, TrainingArguments, T5TokenizerFast
from arguments import DataTrainingArguments
from preprocessing.data_collator import T2TDataCollator

class QGARTrainer:
    def __init__(self, model: Any, data_arguments: DataTrainingArguments, training_arguments: TrainingArguments, tokenizer: T5TokenizerFast):
        self._model = model
        self._data_args = data_arguments
        self._training_arguments = training_arguments
        self._tokenizer = tokenizer

    def setup(self):
        self._trainer = Trainer(
            model=self._model,
            args=self._training_arguments,
            train_dataset=self._data_args.training_file_path,
            eval_dataset=self._data_args.validation_file_path,
            data_collator=T2TDataCollator()
        )

    def train_and_save(self):
        self._trainer.train()
        self._trainer.save_model("./models/")

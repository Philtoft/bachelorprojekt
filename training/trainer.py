import torch
from transformers import Trainer, TrainingArguments, PreTrainedModel, PreTrainedTokenizer
from preprocessing.data_collator import T2TDataCollator

class QGARTrainer:
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer, training_file: str, validation_file: str, training_arguments: TrainingArguments):
        """
        Initializes an instance of QGARTrainer for the given model. 
        The provided model will be trained on the specified training and validation file for the given training arguments.
        """
        
        # Load datasets from files
        train = torch.load(training_file)
        validation = torch.load(validation_file)

        self._tokenizer = tokenizer
        self._trainer = Trainer(
            model=model,
            args=training_arguments,
            train_dataset=train,
            eval_dataset=validation,
            data_collator=T2TDataCollator()
        )
    
    def train(self):
        """Start training the model."""

        self._trainer.train()

        if self._trainer.is_world_process_zero():
            self._tokenizer.push_to_hub("the-coorporation/t5-qgar")

        self._trainer.push_to_hub("the-coorporation/t5-qgar")

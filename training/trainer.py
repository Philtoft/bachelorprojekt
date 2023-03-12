import torch
from transformers import Trainer, TrainingArguments, PreTrainedModel
from preprocessing.data_collator import T2TDataCollator

class QGARTrainer:
    def __init__(self, model: PreTrainedModel, training_file: str, validation_file: str, training_arguments: TrainingArguments):
        """
        Initializes an instance of QGARTrainer for the given model. 
        The provided model will be trained on the specified training and validation file for the given training arguments.
        """
        
        # Load datasets from files
        train = torch.load(training_file)
        validation = torch.load(validation_file)

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

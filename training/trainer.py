import torch
from transformers import Trainer, TrainingArguments
from preprocessing.data_collator import T2TDataCollator

_MODEL_SAVE_PATH = "./models/"

class QGARTrainer:
    def __init__(self, model, training_file: str, validation_file: str, training_arguments: TrainingArguments):
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

    def save(self, path: str = _MODEL_SAVE_PATH):
        """Save the trained model to the specified directory path."""

        self._trainer.save_model(path)

    def train_and_save(self, path: str = _MODEL_SAVE_PATH):
        """Start training the model. Once completed the trained model will be saved to the specified directory path."""

        self.train()
        self.save(path)
        

from dataclasses import dataclass, field

@dataclass
class ModelArguments:
    """A `dataclass` containing settings for the models to use."""

    qg_model_name: str = field(
        metadata={"help": "Path to pretrained qg model or model identifier from huggingface.co/models"}
    )

    tokenizer_name: str = field(
        metadata={"help": "Identifier for a pretrained tokenizer from huggingface"}
    )

    qa_model_name: str = field(
        metadata={"help": "Path to pretrained qa model or model identifier from huggingface.co/models"}
    )


@dataclass
class DataTrainingArguments:
    """A `dataclass` containing meta settings to be used for setting up training of the `QG` model."""
    
    training_file_path: str = field(
        metadata={"help": "Path for cached training dataset"}
    )

    validation_file_path: str = field(
        metadata={"help": "Path for cached validation dataset"}
    )

    wandb_project_name: str = field(
        metadata={"help": "The name of the project to upload wandb results under"}
    )

    dataset: str = field(
        metadata={"help": "The name of the dataset to load"}
    )

    dataset_output_dir: str = field(
        metadata={"help": "The path to the output directory to save locally created datasets"}
    )

    optimized_training: bool = field(
        metadata={"help": "Whether to apply Smart Batching and Mixed Precision Training"}
    )

    upload_to_hub: bool = field(
        metadata={"help": "Whether to upload the model and tokenizer to Huggingface post training"}
    )

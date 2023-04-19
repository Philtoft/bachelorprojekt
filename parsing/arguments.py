from dataclasses import dataclass, field

@dataclass
class ModelArguments:
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

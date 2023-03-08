from dataclasses import dataclass, field

@dataclass
class ModelArguments:
    model_name: str = field(
        metadata={"help": "Path to pretrained model or model identifier from huggingface.co/models"}
    )

    model_type: str = field(
        metadata={"help": "t5 or bart"}
    )

@dataclass
class DataTrainingArguments:
    training_file_path: str = field(
        metadata={"help": "Path for cached training dataset"}
    )

    validation_file_path: str = field(
        metadata={"help": "Path for cached validation dataset"}
    )

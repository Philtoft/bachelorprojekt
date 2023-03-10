import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from arguments import ModelArguments, DataTrainingArguments
from transformers import (
    HfArgumentParser, 
    TrainingArguments, 
    T5Tokenizer, 
    BartTokenizer, 
    T5TokenizerFast,
    T5ForConditionalGeneration
)
from training.trainer import QGARTrainer

MODEL_TYPE_TO_TOKENIZER = {
    "t5": T5Tokenizer,
    "bart": BartTokenizer,
}

def main():
    model_args, data_args, training_args = parse_args()

    if (
        os.path.exists(training_args.output_dir)
        and os.listdir(training_args.output_dir)
        and training_args.do_train
        and not training_args.overwrite_output_dir
    ):
        raise ValueError(
            f"Output directory ({training_args.output_dir}) already exists and is not empty. Use --overwrite_output_dir to overcome."
        )

    model = T5ForConditionalGeneration.from_pretrained(
        pretrained_model_name_or_path=model_args.model_name
    )

    tokenizer = T5TokenizerFast.from_pretrained(model_args.model_name)

    # Initialize trainer
    trainer = QGARTrainer(model, data_args, training_args, tokenizer)
    trainer.setup()
    trainer.train_and_save()

def parse_args() -> tuple[ModelArguments, DataTrainingArguments, TrainingArguments]:
    with open("./settings.json", "r", encoding="utf-8") as file:
        print(file.read())

    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
    return parser.parse_json_file("./settings.json")

if __name__ == "__main__":
    main()
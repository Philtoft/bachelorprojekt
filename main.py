from arguments import ModelArguments, DataTrainingArguments
from transformers import (
    HfArgumentParser, 
    TrainingArguments, 
    T5Tokenizer, 
    BartTokenizer, 
    set_seed, 
    AutoModelForSeq2SeqLM,
    AutoTokenizer
)
from trainer import QGARTrainer
import os

MODEL_TYPE_TO_TOKENIZER = {
    "t5": T5Tokenizer,
    "bart": BartTokenizer,
}


def main():
    with open("settings.json", "r") as file:
        print(file.read())
    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
    model_args, data_args, training_args = parser.parse_json_file(json_file="./settings.json")

    model_args.model_type = model_args.model_type.lower()

    if (
        os.path.exists(training_args.output_dir)
        and os.listdir(training_args.output_dir)
        and training_args.do_train
        and not training_args.overwrite_output_dir
    ):
        raise ValueError(
            f"Output directory ({training_args.output_dir}) already exists and is not empty. Use --overwrite_output_dir to overcome."
        )
    

    # Set seed
    set_seed(training_args.seed)

    # Set project name -> RESEARCH
    os.environ["QGAR"] = "question-generation"

    model = AutoModelForSeq2SeqLM.from_pretrained(
        pretrained_model_name_or_path=model_args.model_name
    )

    tokenizer = T5Tokenizer.from_pretrained(model_args.model_name)

    # Initialize data_collator

    # Initialize trainer
    trainer = QGARTrainer(model, data_args, training_args, tokenizer)
    trainer.setup()
    trainer.train_and_save()



if __name__ == "__main__":
    main()
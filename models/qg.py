from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    TrainingArguments,
    Trainer,
)
from arguments import DataTrainingArguments
from preprocessing.data_collator import T2TDataCollator
import torch
import wandb

_MODEL = "the-coorporation/t5-qg"

class QG:
    """Question Generator model based on T5-small."""

    def __init__(self, model: str = _MODEL, tokenizer: str = _MODEL):
        """Initializes the QG model."""

        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._model: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(model).to(self._device)
        self._tokenizer: PreTrainedTokenizer = AutoTokenizer.from_pretrained(tokenizer, model_max_length=512)

        self._tokenizer.sep_token = '<sep>'
        self._tokenizer.add_tokens(['<sep>'])
        self._model.resize_token_embeddings(len(self._tokenizer))

    def __call__(self, context: str) -> dict[str, str]:
        """Generates questions based on the given context and formats it as a dictionary."""

        generator_args = {
            "max_length": 256,
            "num_beams": 4,
            "length_penalty": 1.5,
            "no_repeat_ngram_size": 3,
            "early_stopping": True,
        }

        input_string = "generate questions: " + context + " </s>"
        input_ids = self._tokenizer.encode(input_string, return_tensors="pt").to(self._device)
        result = self._model.generate(input_ids, **generator_args)
        questions = self._tokenizer.batch_decode(result, skip_special_tokens=True)[0]
        questions = questions.split("<sep>")
        # Remove leading and trailing white space, remove last empty element from results
        questions = [question.strip() for question in questions[:-1]]

        output = {
            "context": context,
            "questions": questions
        }

        return output

    def train(self, training_args: TrainingArguments, data_args: DataTrainingArguments, wandb_key: str):
        """Start training the QG model. Once completed it will be pushed to the HuggingFace Hub."""

        wandb.login(key=wandb_key)

        train = torch.load(data_args.training_file_path)
        validation = torch.load(data_args.validation_file_path)

        trainer = Trainer(
            model=self._model,
            args=training_args,
            train_dataset=train,
            eval_dataset=validation,
            data_collator=T2TDataCollator()
        )

        trainer.train()
        wandb.finish()
        trainer.push_to_hub()

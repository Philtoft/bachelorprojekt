from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    TrainingArguments,
    Trainer,
)
from parsing.settings_parser import DataTrainingArguments
from preprocessing.data_collator import T2TDataCollator
import torch
import wandb
import os

_MODEL_MAX_LENGTH = 512

class QG:
    """Question Generator model based on Google's `T5` model."""

    def __init__(self, model: str, tokenizer: str):
        """Initializes the `QG` model."""

        self._device = "cuda" if torch.cuda.is_available() else "cpu"
        self._model: PreTrainedModel = AutoModelForSeq2SeqLM.from_pretrained(model).to(self._device)
        self._tokenizer: PreTrainedTokenizer = AutoTokenizer.from_pretrained(tokenizer, model_max_length=_MODEL_MAX_LENGTH)

        self._tokenizer.add_tokens(['<sep>'])
        self._model.resize_token_embeddings(len(self._tokenizer))


    def __call__(self, context: str) -> list:
        """Generates questions based on the given context and formats it as a dictionary."""

        generator_args = {
            "max_length": 256,
            "num_beams": 4,
            "length_penalty": 1.5,
            "no_repeat_ngram_size": 3,
            "early_stopping": True,
        }

        # Split the context into chunks of the maximum length
        context_chunks = self.split_text(context)

        context_and_questions = []

        # Generate questions for each chunk
        i = 0
        for context_chunk in context_chunks:
<<<<<<< HEAD
            if i > 5:
=======
            if i > 10:
>>>>>>> main
                break
                
            i += 1

            input_string = "generate questions: " + context_chunk + " </s>"
            
            # Encode input string
            input_ids = self._tokenizer.encode(input_string, return_tensors="pt").to(self._device)

            # Let the model generate questions from the encoded input
            result = self._model.generate(input_ids, **generator_args)

            # Decode the questions generated by the model
            questions = self._tokenizer.decode(result[0], skip_special_tokens=True)

            # Split each question by the separator token
            questions = questions.split("<sep>")

<<<<<<< HEAD
            # If there are multiple '?' in a question, split it into multiple questions
            # TODO: Doesn't create questionmark on each question
            for question in questions:
                if question.count('?') > 1:
                    questions.remove(question)
                    split_questions = question.split('?')
                    split_questions = [newQuestion + '?' for newQuestion in split_questions]
                    questions.extend(split_questions)

=======
>>>>>>> main
            # Remove leading and trailing white space, remove last empty element from results
            questions = [question.strip() for question in questions]

            # Remove empty questions
            questions = [question for question in questions if question != '']

            context_and_questions.append({
                "context": context_chunk,
                "questions": questions
            })

        return context_and_questions

    def split_text(self, text:str, max_length:str=_MODEL_MAX_LENGTH):
        """Splits the given text into chunks of the given maximum length."""
        # todo: need to find correct way of splitting text into chunks in relation to the model's max length
        max_length = max_length / 2
        sentences = text.split(".")
        chunks = []
        current_chunk = ""

        for sentence in sentences:
            tokenized_sentence = self._tokenizer(sentence)

            if len(current_chunk.split()) + len(tokenized_sentence) < max_length:
                current_chunk += f"{sentence}."
            else:
                chunks.append(current_chunk.strip())
                current_chunk = f"{sentence}."

        if current_chunk.strip():
            chunks.append(current_chunk.strip())

        return chunks

    def train(self, training_args: TrainingArguments, data_args: DataTrainingArguments, wandb_key: str):
        """Start training the `QG` model. Once completed it will be pushed to the HuggingFace Hub."""

        os.environ['WANDB_PROJECT'] = data_args.wandb_project_name

        wandb.login(key=wandb_key)

        train = torch.load(data_args.training_file_path)
        validation = torch.load(data_args.validation_file_path)

        trainer = Trainer(
            model=self._model,
            args=training_args,
            train_dataset=train,
            eval_dataset=validation,
            data_collator=T2TDataCollator(self._model, self._tokenizer)
        )

        trainer.train()
        wandb.finish()
        trainer.push_to_hub(blocking=True)
        self._tokenizer.push_to_hub(training_args.hub_model_id)

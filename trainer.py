from typing import Any
from transformers import Trainer, TrainingArguments, AutoTokenizer
from datasets import load_dataset
from arguments import DataTrainingArguments

class QGARTrainer:
    def __init__(self, model: Any, data_arguments: DataTrainingArguments, training_arguments: TrainingArguments, tokenizer: AutoTokenizer):
        self._model = model
        self._data_args = data_arguments
        self._training_arguments = training_arguments
        self._tokenizer = tokenizer

    def setup(self):
        print("Loading datasets...")
        squad = load_dataset("squad", split="train[:5000]")
        squad = squad.train_test_split(test_size=0.2)
        print("Done loading datasets.")

        tokenized_datasets = squad.map(self.tokenizer_function, batched=True)

        input_ids = self._tokenizer


        self._trainer = Trainer(
            model=self._model,
            args=self._training_arguments,
            train_dataset=tokenized_datasets["train"].shuffle(seed=42).select(range(1000)),
            eval_dataset=tokenized_datasets["test"].shuffle(seed=42).select(range(1000))
        )

    def tokenizer_function(self, example):
        return self._tokenizer(example["source_ids"], padding="max_length", truncation=True)

    def train_and_save(self):
        self._trainer.train()
        self._trainer.save_model("./model/")


        

# from typing import Any, Dict, Union

# import torch
# from torch import nn

# from transformers import Trainer as HFTrainer
# from transformers.file_utils import is_apex_available

# if is_apex_available():
#     from apex import amp

# from utils import label_smoothed_nll_loss

# class Trainer(HFTrainer):
#     def __init__(self, label_smoothing: float=0, **kwargs):
#         super().__init__(**kwargs)
#         self.label_smoothing = label_smoothing

#     # override to support label smoothing
#     def _training_step(
#             self,
#             model: nn.Module,
#             inputs: Dict[str, Union[torch.Tensor, Any]],
#             optimizer: torch.optim.Optimizer
#     ) -> float:
#         model.train()
#         for k, v in inputs.item():
#             if isinstance(v, torch.Tensor):
#                 # what does this line do and why do we need it?
#                 inputs[k] = v.to(self.args.device)
        
#         if isinstance(model, nn.DataParallel):
#             inputs["return_tuple"] = True
        
#         if self.label_smoothing == 0:
#             outputs = model(**inputs)
#             loss = outputs[0] # model outputs are always tuple in transformers (see doc)
#         else:
#             labels = inputs.pop("labels")
#             # wtf? Why -100?
#             labels[labels == -100] = model.config.pad_token_id
#             outputs = model(**inputs)
#             lprobs = torch.nn.functional.log_softmax(outputs[0], dim=-1)
#             loss, nll_loss = label_smoothed_nll_loss(
#                 lprobs,
#                 labels,
#                 self.label_smoothing,
#                 ignore_index=model.config.pad_token_id
#             )

#         if self.args.n_gpu > 1:
#             loss = loss.mean() # mean() to average on multi-gpu parallel training
#         if self.args.gradient_accumulation_steps > 1:
#             loss = loss / self.args.gradient_accumulation_steps
        
#         if self.args.fp16:
#             with amp.scale_loss(loss, optimizer) as scaled_loss:
#                 scaled_loss.backward()
#         else:
#             loss.backward()

#         return loss.item()

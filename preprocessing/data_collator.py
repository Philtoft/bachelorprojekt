from dataclasses import dataclass
from transformers import T5TokenizerFast, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM
from transformers.utils import PaddingStrategy, TensorType


@dataclass
class T2TDataCollator(DataCollatorForSeq2Seq):
    """
    A data collator for a text-to-text transformer model, which dynamically pads a batch to the longest
    example length in the batch.
    """

    def __init__(self, model: AutoModelForSeq2SeqLM, tokenizer: T5TokenizerFast, padding: PaddingStrategy = PaddingStrategy.LONGEST):
        super().__init__(model=model, tokenizer=tokenizer, padding=padding, return_tensors=TensorType.PYTORCH)

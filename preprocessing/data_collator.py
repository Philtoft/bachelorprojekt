from dataclasses import dataclass
from transformers import T5TokenizerFast, DataCollatorForSeq2Seq, AutoModelForSeq2SeqLM
from transformers.utils import PaddingStrategy
import torch


@dataclass
class T2TDataCollator():
    """
    A simple data collator for a text-to-text transformer model, which can take a list of samples
    from a dataset and collate them into a batch.
    """

    def __call__(self, batch: list) -> dict[str, torch.Tensor]:
        """
        Take a list of samples from a dataset and collate them into a batch.
        """

        # Convert encoder and decoder input ids to Tensors
        input_ids = torch.stack([example['input_ids'] for example in batch])
        lm_labels = torch.stack([example['decoder_input_ids'] for example in batch])

        # Batched inputs typically differ in length, we therefore need padding by adding a padding token
        # Padding of labels is done with token id -100. This token is automatically ignored by PyTorch's loss functions
        lm_labels[lm_labels[:, :] == 0] = -100
        attention_mask = torch.stack([example['attention_mask'] for example in batch])
        decoder_attention_mask = torch.stack([example['decoder_attention_mask'] for example in batch])

        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': lm_labels,
            'decoder_attention_mask': decoder_attention_mask
        }


@dataclass
class T2TDataCollatorWithDynamicPadding(DataCollatorForSeq2Seq):
    """
    A data collator for a text-to-text transformer model, which dynamically pads a batch to the longest
    example length in the batch.
    """

    def __init__(self, model: AutoModelForSeq2SeqLM, tokenizer: T5TokenizerFast):
        super().__init__(model=model, tokenizer=tokenizer, padding=PaddingStrategy.LONGEST, return_tensors='pt')

from typing import Dict, List, Optional

import torch

def trim_batch(
        input_ids, pad_token_id, attention_mask=None
):
    keep_column_mask = input_ids.ne(pad_token_id).any(dim=0)
    if attention_mask is None:
        return input_ids[:, keep_column_mask]
    else:
        return (input_ids:[:, keep_column_mask], attention_mask[:, keep_column_mask])

class QGARDataCollator():
    def __init__(self, tokenizer, model_type="t5", mode="training", using_tpu=False):
        self.tokenizer = tokenizer
        self.model_type = model_type
        self.mode = mode
        self.using_tpu = using_tpu
    
    def __call__(self, batch: List) -> Dict[str, torch.Tensor]:
        input_ids = torch.stack([example["source_ids"] for example in batch])
        target_ids = torch.stack([example["target_ids"] for example in batch])
        attention_mask = torch.stack([example["attention_mask"] for example in batch])

        pad_token_id = self.tokenizer.pad_token_id

        input_ids, attention_mask = trim_batch(input_ids, pad_token_id, attention_mask=attention_mask)
        target_ids = trim_batch(target_ids, pad_token_id)

        # I assume model is t5
        lm_labels = target_ids.clone()
        decoder_input_ids = self._shift_right_t5(lm_labels)
        if self.mode == "training":
            lm_labels[lm_labels[:,:] == pad_token_id] = -100
        
        params = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": lm_labels,
            "decoder_input_ids": decoder_input_ids
        }

        return params
    
    def _shift_right_t5(self, input_ids):
        decoder_start_token_id = self.tokenizer.pad_token_id
        pad_token_id = self.tokenizer.pad_token_id

        # shift inputs to the right -> WHAT DOES SHIFTING INPUT MEAN in this context??
        shifted_input_ids = input_ids.new_zeros(input_ids.shape)
        shifted_input_ids[...,1:] = input_ids[..., :-1].clone()
        shifted_input_ids[..., 0] = decoder_start_token_id

        shifted_input_ids.masked_fill_(shifted_input_ids == -100, pad_token_id)

        return shifted_input_ids



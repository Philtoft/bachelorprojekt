from ast import List
from dataclasses import dataclass
import torch


@dataclass
class T2TDataCollator():
    """
    A datacollator for a text-to-text transformer model, which can take a list of samples
    from a dataset and collate them into a batch.
    """

    def __call__(self, batch: List) -> dict[str, torch.Tensor]:
        """
        Take a list of samples from a dataset and collate them into a batch.
        Returns:
        A dictionary of tensors.
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


# def pad_seq(seq: List[int], max_batch_len: int, pad_value: int) -> List[int]:
#     # IRL, use pad_sequence
#     # https://pytorch.org/docs/master/generated/torch.nn.utils.rnn.pad_sequence.html
#     return seq + (max_batch_len - len(seq)) * [pad_value]
    
# @dataclass
# class SmartCollator(DataCollator):
#     pad_token_id: int
#     def collate_batch(self, batch: List[Features]) -> Dict[str, torch.Tensor]:
#         batch_inputs = list()
#         batch_attention_masks = list()
#         labels = list()
#         # find the max length of the mini batch
#         max_size = max([len(ex.input_ids) for ex in batch])
#         for item in batch:
#             # apply padding at the mini batch level
#             batch_inputs += [pad_seq(item.input_ids, max_size, self.pad_token_id)]
#             batch_attention_masks += [pad_seq(item.attention_mask, max_size, 0)]
#             labels.append(item.label)
#         # expected Transformers input format (dict of Tensors)
#         return {"input_ids": torch.tensor(batch_inputs, dtype=torch.long),
#                 "attention_mask": torch.tensor(batch_attention_masks, dtype=torch.long),
#                 "labels": torch.tensor(labels, dtype=torch.long)
#                 }
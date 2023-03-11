import torch
from transformers import(
    AutoModelForSeq2SeqLM, 
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
    BatchEncoding
)

_MODEL = "valhalla/t5-base-e2e-qg"

class QGAR:
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer, device: str):
        self._device = device
        self._model = model
        self._tokenizer = tokenizer

    def __call__(self, context: str):
        inputs = self._prepare_inputs_for_qg(context)

        outs = self._model.generate(
            input_ids=inputs['input_ids'].to(self._device),
            attention_mask=inputs['attention_mask'].to(self._device),
        )

        prediction = self._tokenizer.decode(outs[0], skip_special_tokens=True)
        questions = prediction.split("<sep>")
        questions = [question.strip() for question in questions[:-1]]
        return questions

    def _prepare_inputs_for_qg(self, context: str) -> BatchEncoding:
        source_text = f"generate questions: {context} </s>"
        inputs = self._tokenize([source_text], padding=False)
        return inputs
    
    def _tokenize(self, inputs, padding=True, truncation=True, add_special_tokens=True, max_length=512) -> BatchEncoding:
        inputs = self._tokenizer.batch_encode_plus(
            inputs,
            max_length=max_length,
            add_special_tokens=add_special_tokens,
            truncation=truncation,
            padding="max_length" if padding else False,
            pad_to_max_length=padding,
            return_tensors="pt"
        )

        return inputs


def pipeline():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(_MODEL)
    model = AutoModelForSeq2SeqLM.from_pretrained(_MODEL).to(device)

    return QGAR(model=model, tokenizer=tokenizer, device=device)

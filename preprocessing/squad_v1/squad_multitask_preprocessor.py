import json
from datasets import (
    Version,
    builder,
    info,
    download,
    splits,
    features,
    Value
)
import nltk
nltk.download('punkt')

_DESCRIPTION = """\
Stanford Question Answering Dataset (SQuAD) is a reading comprehension \
dataset, consisting of questions posed by crowdworkers on a set of Wikipedia \
articles, where the answer to every question is a segment of text, or span, \
from the corresponding reading passage, or the question might be unanswerable.
"""

_CITATION = """\
@article{2016arXiv160605250R,
       author = {{Rajpurkar}, Pranav and {Zhang}, Jian and {Lopyrev},
                 Konstantin and {Liang}, Percy},
        title = "{SQuAD: 100,000+ Questions for Machine Comprehension of Text}",
      journal = {arXiv e-prints},
         year = 2016,
          eid = {arXiv:1606.05250},
        pages = {arXiv:1606.05250},
archivePrefix = {arXiv},
       eprint = {1606.05250},
}
"""

_SET_URL = "https://rajpurkar.github.io/SQuAD-explorer/dataset/"
_SET_URLS = {
    "train": _SET_URL + "train-v1.1.json",
    "dev": _SET_URL + "dev-v1.1.json"
}

class SquadMultitaskConfig(builder.BuilderConfig):
    """Builder configuration for SQuAD"""

    def __init__(self, **kwargs):
        super(SquadMultitaskConfig, self).__init__(**kwargs)

class SquadMultitaskPreprocessor(builder.GeneratorBasedBuilder):

    BUILDER_CONFIGS = [
        SquadMultitaskConfig(
            name="highlight_qg_format",
            version=Version("1.0.0", ""),
            description="Plain text"
        )
    ]
    
    def _info(self) -> info.DatasetInfo:
        return info.DatasetInfo(
            description=_DESCRIPTION,
            features=features.Features(
            {
                "source_text": Value("string"),
                "target_text": Value("string"),
                "task": Value("string"),
            }
            ),
            # No default supervised_keys (as we have to pass both question
            # and context as input).
            supervised_keys=None,
            homepage="https://rajpurkar.github.io/SQuAD-explorer/",
            citation=_CITATION,
        )
    
    def _split_generators(self, dl_manager: download.DownloadManager):
        """Downloads the specified datasets and splits it in trainining and validation sets"""

        files = dl_manager.download_and_extract(_SET_URLS)

        return [
            splits.SplitGenerator(name=splits.Split.TRAIN, gen_kwargs={"filepath": files["train"]}),
            splits.SplitGenerator(name=splits.Split.VALIDATION, gen_kwargs={"filepath": files["dev"]})
        ]
    
    def _get_correct_alignment(self, context, answer: dict[str, str]) -> tuple[int, int]:
        """
        Some original examples in SQuAD have indices wrong by 1 or 2 character. 
        We test and fix this here.
        """

        text = answer['text']
        start_index: int = answer['answer_start']
        end_index: int = start_index + len(text)

        if context[start_index:end_index] == text:
            return start_index, end_index         # Label position OK
        elif context[start_index - 1:end_index - 1] == text:
            return start_index - 1, end_index - 1 # Label is off by one char
        elif context[start_index - 2: end_index - 2] == text:
            return start_index - 2, end_index - 2 # Label is off by two chars
        else:
            raise ValueError()

    def process_qa_text(self, context, question, answer) -> dict[str, str]:
        input = f"question: {question} context: {context}"
        
        return {
            "source_text": input,
            "target_text": f"{answer}",
            "task": "qa"
        }

    def process_qg_text(self, context, question, answer: dict[str, str]) -> dict[str, str]:
        answer_text = answer['text'].strip()

        start_pos, end_pos = self._get_correct_alignment(context, answer)
        
        # 1. Add task classifier
        # 2. Add context from start to start of answer
        # 3. Insert start highlight token placeholder
        # 4. Insert answer part of context
        # 5. Insert end highlight token placeholder
        # 6. Add rest of context after the answer part
        input = f"generate question: {context[:start_pos]} {{hl_token}} {answer_text} {{hl_token}} {context[end_pos:]}"

        return {
            "source_text": input,
            "target_text": f"{question}",
            "task": "qg"
        }
    
    def process_e2e_qg(self, paragraph) -> dict[str, str]:
        source_text = f"generate questions: {paragraph['context'].strip()}"
        questions = [qas['question'].strip() for qas in paragraph['qas']]
        target_text = " {sep_token} ".join(questions)
        target_text = f"{target_text} {{sep_token}}"

        return {
            "source_text": source_text,
            "target_text": target_text,
            "task": "e2e_qg"
        }
    
    def process_answer_extraction(self, paragraph) -> dict[str, str]:
        """For each sentence in context, add highlight token on sentence containing answer."""

        context = paragraph['context'].strip()

        # Split context in sentences (each sentence is divided by .)
        sentences = nltk.sent_tokenize(context)

        positions = []
        for i, sentence in enumerate(sentences):
            if i == 0:
                start, end = 0, len(sentence)
            else:
                start, end = (prev_end + 1), (prev_end + len(sentence) + 1)
            prev_end = end
            positions.append({
                'start': start,
                'end': end
            })

        answers = [qa['answers'][0] for qa in paragraph['qas']]

        sentence_answers = []
        for pos, sentence in zip(positions, sentences):
            target_answers = []
            for answer in answers:
                if answer['answer_start'] in range(pos['start'], pos['end']):
                    target_answers.append(answer['text'].strip())
            sentence_answers.append(target_answers)
        
        examples = []

        for i, ans in enumerate(sentence_answers):
            context = "extract answers:"
            if len(ans) == 0: continue
            ans = list(set(ans))
            for j, sent in enumerate(sentences):
                if i == j:
                    sent = "{hl_token} %s {hl_token}" % sent
                context = "%s %s" % (context, sent)
                context = context.strip()
            input_text = context
            target_text = " {sep_token} ".join(ans) + " {sep_token}"

            examples.append({
                'source_text': input_text, 
                "target_text": target_text, 
                "task": "ans_ext"
            })
        
        return examples

    
    def _generate_examples(self, filepath):
        count = 0
        tasks = ['qa', 'qg', 'ans_ext', 'e2e_qg']

        with open(filepath) as file:
            squad = json.load(file)

            for article in squad["data"]:
                for paragraph in article['paragraphs']:
                    context = paragraph["context"].strip()

                    if 'ans_ext' in tasks:
                        ans_ext_examples = self.process_answer_extraction(paragraph)
                        for example in ans_ext_examples:
                            yield count, example
                            count += 1

                    if 'e2e_qg' in tasks:
                        yield count, self.process_e2e_qg(paragraph)
                        count += 1

                    for qa in paragraph['qas']:
                        question = qa['question'].strip()

                        answers = [answer['text'].strip() for answer in qa['answers']]
                        
                        for task in tasks:
                            if task == 'qa':
                                yield count, self.process_qa_text(context, question, answers[0])
                                count += 1
                            
                            if task == 'qg':
                                yield count, self.process_qg_text(context, question, qa['answers'][0])
                                count += 1


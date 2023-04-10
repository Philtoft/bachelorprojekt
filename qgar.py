from bs4 import BeautifulSoup
from markdown import markdown
from transformers import pipeline
from models.qg import QG
import json
import re

_CURRENT_STUDENT = "Una"

class qgar():
    """
    This class has the following tasks:
    - Insert raw student notes into a notes folder
    - Parse and clean notes
    - Insert notes into the QG model
    - Combine all the questions into one array of questions 
    - Insert questions into the QA model (distilbert-base-**uncased**-squad)
    - Sort the answers based on certainty score
    - Select top 20 most certain question and answers
    - Output the results in a CSV file
    """

    def __init__(self):
        self._qg = QG("the-coorporation/t5-small-qg", "the-coorporation/t5-small-qg")
        self._qa = pipeline("question-answering", "distilbert-base-uncased-distilled-squad")
        self._context_and_questions = []
        self._questions_and_answeres = []
        self._context = ""
        # self.qa = 

    def parse_notes(self, student:str, notetype: str = "md"):
        with open(f"./data/notes/{student}/{student}.{notetype}") as fp:
            notes = fp.read()
        if notetype == "md":
            notes = self.markdown_to_html(notes)
        plaintext = self.html_to_plaintext(notes)
        return plaintext
    

    def markdown_to_html(self, markdown_notes: str):
        """ Converts a markdown string to HTML """
        result = markdown(markdown_notes)
        return result
        
    def html_to_plaintext(self, html_notes: str):
        """ Converts a markdown string to plaintext """
        soup = BeautifulSoup(html_notes, "html.parser")
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            h_tag.decompose()
        result = ' '.join(soup.stripped_strings)
        result = result.replace("\n", " ")
        result = result.replace("\t", " ")
        result = re.sub("\s\s+", " ", result)
        return result

    def generate_questions(self, plaintext_notes: str):
        """ Generates questions from the notes """
        questions_and_contexts = self._qg(plaintext_notes)
        return questions_and_contexts
    
    def generate_answers(self, questions_and_contexts):
        """ Generates answers from the notes """
        questions_ans_answers = []
        for questions_and_context in questions_and_contexts:
            context, questions = questions_and_context.values()
            for question in questions:
                answer = self._qa(context=context, question=question)
                questions_ans_answers.append({
                    "context": context,
                    "question": question,
                    "answer": answer
                })

        return questions_ans_answers

    def sort_answers(self, questions_and_answers):
        """ Sorts the answers based on certainty score """
        sorted_answers = sorted(questions_and_answers, key=lambda x: x["answer"]["score"], reverse=True)
        return sorted_answers

    def output_questions_answers(self, plaintext_notes: str):
        """ Outputs the questions and answers to a file """
        questions_and_contexts = self.generate_questions(plaintext_notes)
        questions_and_answers = self.generate_answers(questions_and_contexts)
        # TODO: Get the top 20 most certain answers
        return questions_and_answers


# Make the user having to define qg model name and qa model name
qga = qgar()
plaintext = qga.parse_notes(_CURRENT_STUDENT, "html")
all_questions_and_answers = qga.output_questions_answers(plaintext)
final_questions_answers = qga.sort_answers(all_questions_and_answers)
with open(f"./data/notes/{_CURRENT_STUDENT}/{_CURRENT_STUDENT}-questions-and-answers.json", "w") as fp:
    json.dump(final_questions_answers, fp)

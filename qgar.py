from bs4 import BeautifulSoup
from markdown import markdown
from transformers import pipeline
from models.qg import QG
import json


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
        self._qg = QG("the-coorporation/t5-qgar", "t5-small")
        self._qa = pipeline("question-answering")
        self._context_and_questions = []
        self._questions_and_answeres = []
        self._context = ""
        # self.qa = 

    def parse_notes(self, notename: str):
        # 1) Get notes from file
        with open(f"./data/notes/{notename}.md") as fp:
            notes = fp.read()
        html_notes = self.markdown_to_html(notes)
        plaintext = self.html_to_plaintext(html_notes)
        return plaintext

    def markdown_to_html(self, markdown_notes: str):
        """ Converts a markdown string to HTML """
        result = markdown(markdown_notes)
        return result
        
    def html_to_plaintext(self, html_notes: str):
        """ Converts a markdown string to plaintext """
        soup = BeautifulSoup(html_notes, "html.parser")
        result = ' '.join(soup.stripped_strings)
        return result

    def generate_questions(self, plaintext_notes: str):
        """ Generates questions from the notes """
        questions_and_context = self._qg(plaintext_notes)
        return questions_and_context
    
    def generate_answers(self, questions_and_context):
        """ Generates answers from the notes """
        questions_ans_answers = []
        for question_and_context in questions_and_context:
            context, question = question_and_context.values()
            answer = self._qa(context=context, question=question)
            questions_ans_answers.append({
                "question": question,
                "answer": answer
            })
        return questions_ans_answers

    def sort_answers(self):
        """ Sorts the answers based on certainty score """
        pass

    def output_questions_answers(self, plaintext_notes: str):
        """ Outputs the questions and answers to a file """
        questions_and_context = self.generate_questions(plaintext_notes)
        questions_and_answers = self.generate_answers(questions_and_context)
        # TODO: Get the top 20 most certain answers
        return questions_and_answers


# Make the user having to define qg model name and qa model name
my_qgar = qgar()
plaintext = my_qgar.parse_notes("thhs")
questions_and_answers = my_qgar.output_questions_answers(plaintext)
with open("questions_and_answers.json", "w") as fp:
    json.dump(questions_and_answers, fp)

# my_qgar.generate_questions()
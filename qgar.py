from bs4 import BeautifulSoup
from markdown import markdown
import re
from transformers
from models.qg import QG


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

    def __init__(self, notes: str):
        self._notes = notes
        self._qg = QG("the-coorporation/t5-qgar", "t5-small")
        self._qa = 
        self._context_and_questions = []
        self._question_answers = []
        self._context = ""
        # self.qa = 

    def parse_notes(self):
        # 1) Get notes from file
        with open(f"./data/notes/{self._notes}.md") as fp:
            self._notes = fp.read()
        self.markdown_to_html()
        self.html_to_plaintext()

    def markdown_to_html(self):
        """ Converts a markdown string to HTML """
        result = markdown(self._notes)
        self._notes = result
        
    def html_to_plaintext(self):
        """ Converts a markdown string to plaintext """
        soup = BeautifulSoup(self._notes, "html.parser")
        result = ' '.join(soup.stripped_strings)
        self._notes = result

    def generate_questions(self):
        """ Generates questions from the notes """
        questions = self._qg(self._notes)
        # TODO: Include context for each question
        self._context_and_questions = questions[]
        return questions
    
    def generate_answers(self):
        """ Generates answers from the notes """
        pass

    def output_questions_answers(self):
        """ Outputs the questions and answers to a file """
        pass


my_qgar = qgar("thhs")
my_qgar.parse_notes()
questions = my_qgar.generate_questions()
print(f"Questions: {questions}")

# my_qgar.generate_questions()
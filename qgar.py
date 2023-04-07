from bs4 import BeautifulSoup
from markdown import markdown
import re

from models.qg import QG


class qgar():
    """
    This class has the following tasks:
    - [] Parses and cleans students notes
    - Inserts the notes into the QG model

    """

    def __init__(self, notes: str):
        self.notes = notes
        # self.qg = QG("t5-small", "t5-small")
        # self.qa = 

    def parse_notes(self):
        # 1) Get notes from file
        with open(f"./data/notes/{self.notes}.md") as fp:
            self.notes = fp.read()
        self.markdown_to_html()
        self.html_to_plaintext()

    def markdown_to_html(self):
        """ Converts a markdown string to HTML """
        result = markdown(self.notes)
        self.notes = result
        
    def html_to_plaintext(self):
        """ Converts a markdown string to plaintext """
        soup = BeautifulSoup(self.notes, "html.parser")
        result = ' '.join(soup.stripped_strings)
        self.notes = result

    def generate_questions(self):
        """ Generates questions from the notes """
        questions = self.qg(self.notes)
    
    def generate_answers(self):
        """ Generates answers from the notes """
        pass

    def output_questions_answers(self):
        """ Outputs the questions and answers to a file """
        pass


my_qgar = qgar("thhs")
my_qgar.parse_notes()
print(my_qgar.notes)

# my_qgar.generate_questions()
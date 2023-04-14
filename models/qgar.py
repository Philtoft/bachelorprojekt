from bs4 import BeautifulSoup
from markdown import markdown
from transformers import pipeline
from models.qg import QG
import json
import re
import os
import pathlib
import html
import logging

logging.basicConfig(level=logging.INFO, filename="qgar.log", filemode="a", format='%(asctime)s %(message)s')

_FILE_TYPES = [".md", ".html"]
_NOTE_DIR = "data/notes"


class QGAR:
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

    def __init__(self, qg: QG, qa: str):
        """ Initializes a new instance of the QGAR pipeline. """

        self._qg = qg
        self._qa = pipeline("question-answering", qa)

    def __call__(self, student: str):
        """
        Generates questions and answers and saves them in json format. 

        QGAR:
        1. Loads a note in either markdown or HTML format
        2. Generates questions and answers
        3. Saves them as `<student>.json` to disk
        """

        plaintext = self._parse_notes(student)
        qgas = self._generate_questions_answers(plaintext)

        with open(f"{_NOTE_DIR}/{student}/{student}-questions-and-answers.json", "w") as file:
            json.dump(qgas, file)

    def _parse_notes(self, student: str):
        notetype = self._get_note_type(student)

        with open(f"{_NOTE_DIR}/{student}/{student}{notetype}") as file:
            notes = file.read()
        if notetype == ".md":
            notes = self._markdown_to_html(notes)

        plaintext = self._html_to_plaintext(notes)

        return plaintext

    def _get_note_type(self, student: str):
        for file in os.listdir(f"{_NOTE_DIR}/{student}/"):
            suffix = pathlib.Path(file).suffix
            if suffix in _FILE_TYPES:
                return suffix

        raise FileNotFoundError(f"No supported filetypes found in directory '{student}'")

    def _markdown_to_html(self, markdown_notes: str):
        """ Converts a markdown string to HTML """

        escaped_markdown = html.escape(markdown_notes)
        return markdown(escaped_markdown)

    def add_colon_if_last_char_not_dot(self, text: str):
        if text[-1] != "." and text[-1] != ":":
            text += ":"
        return text
    
    def add_dot_if_last_char_not_dot(self, text: str):
        if text[-1] != "." and  text[-1] != ":":
            text += "."
        return text

    def _html_to_plaintext(self, html_notes: str):
        """ Converts a markdown string to plaintext """

        soup = BeautifulSoup(html_notes, "html.parser")
        for h_tag in soup.find_all(["h1", "h2", "h3"]):
            # add_dot_if_last_char_not_dot(h_tag.text)
            # h_tag.decompose()
            h_tag.string = self.add_dot_if_last_char_not_dot(h_tag.text)

        # On all tags add dor if last c
        for tag in soup.find_all():
            tag.string = self.add_dot_if_last_char_not_dot(tag.text)

        result = ' '.join(soup.stripped_strings)
        result = result.replace("\n", " ")
        result = result.replace("\t", " ")
        result = re.sub("\s\s+", " ", result)
        return result

    def _generate_answers(self, questions_and_contexts: list[dict]) -> list:
        """ Generates answers from the notes """

        questions_and_answers = []
        for questions_and_context in questions_and_contexts:
            context, questions = questions_and_context.values()

            result = {
                "context": context,
                "questions_answers": []
            }

            for question in questions:
                answer = self._qa(context=context, question=question)
                result["questions_answers"].append({
                    "question": question,
                    "answer": answer
                })

            questions_and_answers.append(result)

        # Aggregate score value
        scores = []
        for qa in questions_and_answers:
            for q_a in qa["questions_answers"]:
                scores.append(q_a["answer"]["score"])

        # Print score average
        print(f"Score average: {sum(scores) / len(scores)}")
        logging.info(f"Score average: {sum(scores) / len(scores)}")

        return questions_and_answers

    def _generate_questions_answers(self, plaintext_notes: str):
        """ Outputs the questions and answers to a file """

        questions_and_contexts = self._qg(plaintext_notes)
        questions_and_answers = self._generate_answers(questions_and_contexts)

        return questions_and_answers

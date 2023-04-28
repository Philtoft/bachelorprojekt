from transformers import pipeline
from models.qg import QG
import json
import logging
import pathlib
from parsing.note_parser import NoteParser

logging.basicConfig(level=logging.INFO, filename="qgar.log", filemode="a", format='%(asctime)s %(message)s')


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
        self.student_name = None


    def __call__(self, file_path: str) -> list:
        """
        Generates questions and answers and saves them in json format. 

        QGAR:
        1. Loads a note in either markdown or HTML format
        2. Generates questions and answers
        3. Saves them as `<student>.json` to disk
        """
        note_parser = NoteParser() 
        plaintext = note_parser(file_path)
        qgas = self._generate_questions_answers(plaintext)

        path = pathlib.Path(file_path)
        out_dir = str(path.parent)
        file_name = path.stem
        
        with open(f"{out_dir}/{file_name}-questions-and-answers.json", "w") as file:
            json.dump(qgas, file, indent=4)

        return qgas


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
        logging.info(
            f"Score average: {sum(scores) / len(scores)} - notes from {self.student_name}")

        return questions_and_answers


    def _generate_questions_answers(self, plaintext_notes: str) -> list:
        """ Outputs the questions and answers to a file """

        questions_and_contexts = self._qg(plaintext_notes)
        questions_and_answers = self._generate_answers(questions_and_contexts)

        return questions_and_answers

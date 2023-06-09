import sys
from transformers import pipeline
from models.qg import QG
import json
import logging
import pathlib
import pandas as pd
from parsing.note_parser import NoteParser
from exceptions.exceptions import NoSupportedFileTypeFoundError 


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt="%Y-%m-%d - %H:%M:%S")
logger.propagate = False

file_handler = logging.FileHandler('qgar.log', mode='a')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(ch)


_SUPPORTED_FORMATS = ['csv', 'json']

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


    def __call__(self, file_path: str, out_format: str) -> list:
        """
        Generates questions and answers and saves them in json format. 

        QGAR:
        1. Loads a note in either markdown or HTML format
        2. Generates questions and answers
        3. Saves them as `file_path.json` or `file_path.csv` to disk
        """
        note_parser = NoteParser() 
        plaintext = note_parser(file_path)

        if out_format in _SUPPORTED_FORMATS:
            qas = self._generate_questions_answers(plaintext)

            path = pathlib.Path(file_path)
            out_dir = str(path.parent)
            out_path = f"{out_dir}/{path.stem}"

            if out_format == 'json':
                self._dump_json(qas, out_path)
            
            if out_format == 'csv':
                self._dump_csv(qas, out_path)

            return qas
        
        raise NoSupportedFileTypeFoundError(out_format)


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
        logging.info(f"Score average: {sum(scores) / len(scores)}")

        return questions_and_answers


    def _generate_questions_answers(self, plaintext_notes: str) -> list:
        """ Outputs the questions and answers to a file """

        questions_and_contexts = self._qg(plaintext_notes)
        questions_and_answers = self._generate_answers(questions_and_contexts)

        return questions_and_answers


    def _dump_json(self, qas: list[dict], out_path: str) -> None:
        """ Dumps the genreated questions and answers to a `JSON` file. """

        logger.info(f"Dumping {len(qas)} entries to csv...")
        
        with open(f"{out_path}-questions-and-answers.json", "w") as file:
                json.dump(qas, file, indent=4)
        
        logger.info("Done.")


    def _dump_csv(self, qas: list[dict], out_path: str) -> None:
        """ Dumps the generated questions and answers to a `CSV` file. """
        
        converted_data = [{"question": qa["question"], "answer": qa["answer"]['answer']} for item in qas for qa in item["questions_answers"]]
        logger.info(f"Dumping {len(converted_data)} entries to csv...")
        
        df = pd.DataFrame(converted_data, columns=["question", "answer"])
        
        df.to_csv(f"{out_path}.csv", index=False, header=False)
        logger.info("Done.")

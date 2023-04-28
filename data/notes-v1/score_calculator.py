import argparse
import json
import logging


def main(args: argparse.Namespace, no_arguments: bool):
    if no_arguments:
        parser.print_help()
    else:
        if args.student:
            filename = f"{args.student}/{args.student}-score.log"

            logging.basicConfig(level=logging.INFO, filename=filename,
                                filemode="a", format='%(asctime)s %(message)s')

            with open(f'{args.student}/{args.student}-questions-and-answers.json', "r") as file:
                data = json.load(file)

                score = []

                for qa in data:
                    for q_a in qa["questions_answers"]:
                        score.append(q_a["answer"]["score"])

                print(f"Score average: {sum(score) / len(score)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--student", type=str,
                        help="Specify the student name.")

    main(parser.parse_args(), no_arguments=not len(parser.parse_args().__dict__))

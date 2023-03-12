# Bachelor Project

## Setup before running

The `QGARTrainer` automatically pushes the model post training to Huggingface Hub.

Therefore you must create a `.local` directory in the root directory.

In the `.local` directory create a file called `token.txt` containing your personal access token to Huggingface Hub.

Once the training has commenced, the model will be pushed to `The Cooporation` organization.

## Run main.py

`main.py` can take arguments to specify what to do:

* `main.py -t` starts a training session for the `QGAR` model.
* `main.py -i <text>` runs the `QGAR` model on the input text and generates questions from the given context.
* `main.py -h` shows instructions on how to run the program

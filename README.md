# Bachelor Project

## Setup before running

The `QG` model automatically pushes the model post training to Huggingface Hub if you provide an access token.

Therefore you must create a `.local` directory in the root directory.

In the `.local` directory create a file called `hg_token.txt` containing your personal access token to Huggingface Hub.

Once the training has commenced, the model will be pushed to `The Coorporation` organization.

## Run main.py

`main.py` can take arguments to specify what to do:

- `main.py -t` starts a training session for the `QG` model.
- `main.py -i <text>` runs the `QG` model on the input text and generates questions from the given context.
- `main.py -d` downloads and preprocesses our modified `SQuAD` dataset
- `main.py -n <name>` creates questions and answers and saves it under `<name>.json`
- `main.py -s <settings>.json` use the specified settings file. Defaults to `settings.json`
- `main.py -h` shows instructions on how to run the program

</br>

---

</br>

## Setup Environment

The following sections describe the setup process to use Hugging Face and PyTorch locally on your device.

The steps have been tested to run without errors on `Linux 22.04 (LTS)`.

</br>

## Table of Contents

1. [Setup Miniconda](#setup-miniconda)
2. [Install PyTorch with NVIDIA GPU](#install-pytorch-with-nvidia-gpu)
3. [Install HuggingFace Transformers](#install-huggingface-transformers)
4. [Configure VS Code to use Virtual Environment](#configure-vs-code-to-use-virtual-environment)
5. [Setup on MAC M1](#running-on-apple-silicon-m1)

</br>

---

</br>

## Setup Miniconda

1. Install Miniconda

   Miniconda will be in charge of managing our virtual Python environment and will download and install needed packages.

   To install it, run the commands:

   ```bash
   curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh

   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. Create Virtual Environment

   To isolate our development environment from the main Python installation on your system, we will create a virtual environment.

   In this, we will install all the needed Python packages, which will only be available through the environment.

   Run the following command, where `<name>` is the name of your local environment:

   ```bash
   conda create --name <name> python=3.10.9
   ```

3. Activate the Virtual Environment

   Now we must activate our created environment, so all install commands targets the virtual environment and not your main installation.

   Run the following command, where `<name>` is the name of the virtual environment you created in step 2.

   ```bash
   conda activate <name>
   ```

   In the terminal you should now see the name of your local environment. This way you always know if it is activated.

</br>

---

</br>

### Install PyTorch with NVIDIA GPU

1. Activate your Virtual Environment

   First, make sure you have activated your virtual environment.

   You can activate it with the following command, where `<name>` is the name of the environment:

   ```bash
   conda activate <name>
   ```

2. Install PyTorch

   Run the following command:

   ```bash
   conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
   ```

3. Verify the installation

   Run the following command:

   ```bash
   python3 -c "import torch; print(torch.cuda.is_available())"
   ```

   It should return `True` in the console!

---

</br>

---

### Install HuggingFace Transformers

1. Activate your Virtual Environment

   First, make sure you have activated your virtual environment.

   You can activate it with the following command, where `<name>` is the name of the environment:

   ```bash
   conda activate <name>
   ```

2. Install Transformers

   Run the following command:

   ```bash
   conda install -c huggingface transformers
   ```

3. Verify installation

   Run the following command:

   ```bash
   python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
   ```

   It should output something similar to the following:

   ```txt
   [{'label': 'POSITIVE', 'score': 0.9998704791069031}]
   ```

</br>

---

</br>

### Configure VS Code to use Virtual Environment

1. Open example.py to activate the VS Code Python Extension.
2. Press the `F1` key on your keyboard
3. Write the following:

   ```txt
   > Python: Select Interpreter
   ```

4. Select the interpreter with the name of your local environment (listed as `conda`).
5. The libraries you have installed are now imported correctly.

</br>

---

</br>

## Running on Apple Silicon (M1)

Follow instructions here [link](https://www.youtube.com/watch?v=17gDhXU55oU)

to run, remember to use

```bash
python3 [file].py
```

And not just "python"

To install packages, use

```bash
python3 -m pip install [package]
```

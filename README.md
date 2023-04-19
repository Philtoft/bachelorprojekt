# QGAR - Question Generation Answering RRR

Welcome to the `QGAR Project` - a flashcard generation application.

If you want to run the application please read the [Prerequisites section](#1-prerequisites).

</br>

## Table of Contents

* [1. Prerequisites](#1-prerequisites)
  * [1.1 Create Access Token Files](#11-create-access-token-files)
  * [1.2 Install Dependencies](#12-install-dependencies)
* [2. Run QGAR](#2-run-qgar)
* [3. Setup Virtual Environment](#3-setup-virtual-environment)

---

## 1. Prerequisites

</br>

### 1.1 Create Access Token Files

To get access to our models and datasets you must be a part of our organization, [The Coorporation](https://huggingface.co/the-coorporation), on Huggingface Hub.

Moreover, when training the `QG` model, the training process will be uploaded to [wandb](wandb.ai).

In order for the `QGAR` to do the above, you must be authorized via access tokens.

Therefore you must create a `.local` directory in the root directory and create the following files containing your tokens:

* `hg_token.txt` - contains your access token to Huggingface
* `wandb_token.txt` - contains your access token to Weight and Biases

</br>

### 1.2 Install Dependencies

`QGAR` uses 3rd party libraries which are specified in [requirements.txt](requirements.txt).

To install them either use the command `make install` or:

```txt
pip install -r requirements.txt
```

**NB:** Make sure you install the libraries in a [Virtual Environment](#3-setup-virtual-environment)!

</br>

---

</br>

## 2. Run QGAR

You run `QGAR` by running `main.py` via:

```txt
python main.py <args>
```

The application can take arguments to specify what to do:

* `main.py -t` - starts a training session for the `QG` model.
* `main.py -i <text>` - runs the `QG` model on the input text and generates questions from the given context.
* `main.py -d` - downloads and preprocesses our modified `SQuAD` dataset
* `main.py -n <name>` - creates questions and answers and saves it under `<name>.json`
* `main.py -s <filename>.json` - use the specified settings file. Defaults to `settings.json`
* `main.py -h` -  shows instructions on how to run the program

</br>

---

</br>

## 3. Setup Virtual Environment

The following sections describe the setup process to use Hugging Face and PyTorch locally on your device running in a Virtual Environment.

The steps have been tested to run without errors on `Linux 22.04 (LTS)`.

</br>

**Table of Contents:**

* [3.1 Setup Miniconda](#31-setup-miniconda)
* [3.2 Install PyTorch with NVIDIA GPU](#32-install-pytorch-with-nvidia-gpu)
* [3.3 Install HuggingFace Transformers](#33-install-huggingface-transformers)
* [3.4 Configure VS Code to use Virtual Environment](#34-configure-vs-code-to-use-virtual-environment)
* [3.5 Setup on MAC M1](#35-running-on-apple-silicon-m1)

</br>

---

</br>

## 3.1 Setup Miniconda

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

### 3.2 Install PyTorch with NVIDIA GPU

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

### 3.3 Install HuggingFace Transformers

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

### 3.4 Configure VS Code to use Virtual Environment

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

## 3.5 Running on Apple Silicon (M1)

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

</br>

---

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

</br>

---

</br>

## Setup Environment

The following sections describe the setup process to use Huggingface locally on your `Linux` device.

</br>

## Table of Contents

1. [Setup Miniconda](#setup-miniconda)
2. [Install TensorFlow with NVIDIA GPU](#install-tensorflow-with-nvidia-gpu)
3. [Install PyTorch with NVIDIA GPU](#install-pytorch-with-nvidia-gpu)
4. [Install HuggingFace Transformers](#install-huggingface-transformers)
5. [Configure VS Code to use Virtual Environment](#configure-vs-code-to-use-virtual-environment)
6. [Run Example.py](#run-examplepy)

</br>

---

</br>

## Setup Miniconda

1. Install Miniconda

   Run the commands:

   ```bash
   curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh

   bash Miniconda3-latest-Linux-x86_64.sh
   ```

2. Create Virtual Environment

   Run the following command, where `<name>` is the name of your local environment:

   ```bash
   conda create --name <name> python=3.10.6
   ```

3. Activate the Local Environment

   Run the following command, where `<name>` is the name of the Local Environment you created in step 2.

   ```bash
   conda activate <name>
   ```

</br>

---

</br>

### Install TensorFlow with NVIDIA GPU

If you have an `NVIDIA GPU` on your local machine, you can setup Tensorflow to utilize it instead of the CPU, yielding faster computations.

1. Activate your Local Environment

   First, make sure you have activated your local environment.

   You can activate it with the following command, where `<name>` is the name of the environment:

   ```bash
   conda activate <name>
   ```

2. Check that you have an NVIDIA GPU Driver installed

   Run the command:

   ```bash
   nvidia-smi
   ```

   The command works if it does not return an error!

3. Install CUDA and cuDNN with conda

   Run the command:

   ```bash
   conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
   ```

4. Configure System Path to CUDA libraries

   Run the following commands:

   ```bash
   mkdir -p $CONDA_PREFIX/etc/conda/activate.d

   echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
   ```

   Then deactivate and reactivate your Local Environment, where `<name>` is the name of the created Local Environment:

   ```bash
   conda deactivate
   conda activate <name>
   ```

5. Setup Environment Variables

    Run the following two commands:

    ```bash
    mkdir -p $CONDA_PREFIX/etc/conda/activate.d
    echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
    ```

6. Install TensorFlow

   Run the following commands:

   ```bash
   pip install tensorflow
   ```

7. Verify TensorFlow install

   **CPU Verification:**

   Run the following command:

   ```bash
   python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
   ```

   The command should produce something like the following output the last line:

   ```txt
   tf.Tensor(210.42346, shape=(), dtype=float32)
   ```

   **GPU Verification:**

   Run the following command:

   ```bash
   python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
   ```

   The command should return smething like the following output on the last line:

   ```txt
   [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
   ```

</br>

---

</br>

### Install PyTorch with NVIDIA GPU

1. Activate your Local Environment

   First, make sure you have activated your local environment.

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

1. Activate your Local Environment

   First, make sure you have activated your local environment.

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

## Run `Example.py`

1. First, activate your conda Local Environment, where `<name>` is the name of your environment:

   ```bash
   conda activate <name>
   ```

2. Now let's try to run `example.py` by running the command:

   ```bash
   python example.py
   ```

   It will probably complain about a missing library called `chardet`. Install it with:

   ```bash
   pip install chardet
   ```

3. Now, try to re-run `example.py`. It should output somethin like:

   ```txt
   {'input_ids': tensor([[  101,  1045,  1005,  2310,  2042,  3403,  2005,  1037, 17662, 12172,
           2607,  2026,  2972,  2166,   102],
           [  101,  1045,  5223,  2023,  2061,  2172,   102,     0,     0,     0,
               0,     0,     0,     0,     0]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]])}
   ```

</br>

---

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

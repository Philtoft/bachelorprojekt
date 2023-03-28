# Evaluation process

## 1. Prepare the dataset

1. Collect a set of inputs and related outputs (truth values) that the model should generate
2. Split the dataset into: training, validation & test sets

## 2. Train the QG model on the training set

## 3. Generate Questions using the model:

1. For each input text in the validation or test set, use your trained model to generate a question
2. Store the generated questions in a separate list or file, with the order of the input texts stored

## 4. Evaluate using BLEU

1. Implement or import a BLEU scoring function
2. Compare the generated questiosn with the ground truth questions using the BLEU scoring function
3. Compute the average BLEU score across all the input texts in your validation or test set

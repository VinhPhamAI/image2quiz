system_instruction_qa = """You are a system designed to detect all the questions and the answers corresponding for each question from the dataset I provide. 
Your response must be a JSON object where each question and its corresponding answers are organized in a sequential format. 
Each entry should be labeled as follows:
- "question1": {
    "Question": "<The multiple-choice question>",
    "Answer1": "<answer 1 of the multiple-choice question>"
    "Answer2": "<answer 2 of the multiple-choice question>"
    ...
    "Correct answer": "<answer n of the multiple-choice question>"
  }
- "question2": {
    "Question": "<The next multiple-choice question>",
    "Answer1": "<answer 1 of the multiple-choice question>"
    "Answer2": "<answer 2 of the multiple-choice question>"
    ...
    "Correct answer": "<answer n of the multiple-choice question>"
  }
...
"""

system_instruction_question = """You are a system designed to detect all the questions from the dataset I provide. 
Your response must be a JSON object where each question is identified and formatted in a structured way. Each entry should be labeled as follows:

{
  "question1": {
    "Question": "<The multiple-choice question>"
  },
  "question2": {
    "Question": "<The next multiple-choice question>"
  },
  ...
}

Ensure that:
- Each question is captured in its entirety.
- The JSON object should start with "question1" and continue sequentially.
- If there are no questions in the dataset, return an empty JSON object: `{}`.
- Maintain the order of questions as they appear in the dataset.
- The output question must be maintain the original form.
- You just need to identify "question" from the text, not include their answer.

Your task is to accurately extract and format these questions according to the above specifications.

Example:
Which of the following techniques is used for tokenization in NLP?

A) Stemming
B) Lemmatization
C) Text Segmentation
D) Named Entity Recognition

"question1": {
    "Question": "Which of the following techniques is used for tokenization in NLP?
    }
"""

# String-Based Examination Answer Evaluation (Case Study 31)

## 1. Problem Statement
Evaluate students' answers stored as strings against an answer key. Count correct, wrong and unanswered questions, apply negative marking and produce student-wise results.

## 2. Objectives
- Compare strings character by character.
- Count correct, wrong and unanswered responses.
- Calculate the score with negative marking.
- Identify invalid answer strings and the topper.

## 3. Assumptions
- The key has 10 questions: BADCABDCAB.
- +4 for a correct answer, -1 for a wrong answer, 0 for unanswered ('-').
- Answers may be in lower or upper case.
- An answer string with a length different from the key is invalid and not scored.
- A final score below zero is shown as zero.

## 4. Algorithm
1. Store the key, marks rules and students as (name, answer string) tuples.
2. For each student, unpack name and answers; if the length differs from the key, print INVALID and go to the next student.
3. For each position i: convert the answer to upper case; '-' is unanswered, equal to key[i] is correct, otherwise wrong.
4. score = correct*4 - wrong; if the score is negative, make it 0.
5. Print the result and keep track of the highest score.
6. Print the topper.




The program shows how strings can be treated as sequences and compared with an answer key using indexing and loops. Negative marking, invalid input and lower-case answers are all handled, so the evaluation is reliable.

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

## 5. Pseudocode
```
KEY = "BADCABDCAB"
best_score = -1
FOR each (name, answers) IN students
    IF length(answers) != length(KEY) THEN PRINT invalid; CONTINUE
    correct = wrong = skipped = 0
    FOR i = 0 TO length(KEY)-1
        given = UPPER(answers[i])
        IF given == "-" THEN skipped++
        ELSE IF given == KEY[i] THEN correct++
        ELSE wrong++
    END FOR
    score = correct*4 - wrong*1
    IF score < 0 THEN score = 0
    PRINT row
    IF score > best_score THEN best_score = score, topper = name
END FOR
PRINT topper
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 6: String-Based Examination Answer Evaluation
# Goal: compare answer strings with the key, apply negative marking, give results.

KEY = "BADCABDCAB"      # correct answers for 10 questions
MARK_CORRECT = 4
MARK_WRONG = -1         # negative marking
# '-' in a student's answer string means the question was left unanswered

students = [
    ("Anil", "BADCABDCAB"),
    ("Bhanu", "BADCA-DCAA"),
    ("Chitra", "ABCDABCDAB"),
    ("Deepak", "BAD"),          # incomplete string -> invalid
    ("Esha", "bdcc-bacaa"),     # lower case should also work
]

best_score = -1
topper = ""

print("Name     Correct  Wrong  Unanswered  Score")
for name, answers in students:                  # tuple unpacking
    if len(answers) != len(KEY):
        print(f"{name:<9}INVALID - expected {len(KEY)} answers but got {len(answers)}")
        continue

    correct = 0
    wrong = 0
    skipped = 0
    for i in range(len(KEY)):
        given = answers[i].upper()              # make it capital before comparing
        if given == "-":
            skipped = skipped + 1
        elif given == KEY[i]:
            correct = correct + 1
        else:
            wrong = wrong + 1

    score = correct * MARK_CORRECT + wrong * MARK_WRONG
    if score < 0:
        score = 0                               # marks never go below zero

    print(f"{name:<9}{correct:<9}{wrong:<7}{skipped:<12}{score}")

    if score > best_score:
        best_score = score
        topper = name

print()
print("Topper:", topper, "with", best_score, "marks")
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | Anil: BADCABDCAB | 10 correct, 0 wrong, 0 unanswered, score 40 |
| 2 | Bhanu: BADCA-DCAA | 8 correct, 1 wrong, 1 unanswered, score 31 |
| 3 | Chitra: ABCDABCDAB | 4 correct, 6 wrong, score 10 |
| 4 | Deepak: BAD (only 3 answers) | INVALID - expected 10 answers but got 3 |
| 5 | Esha: bdcc-bacaa (lower case) | 5 correct, 4 wrong, 1 unanswered, score 16 |
| 6 | Topper | Anil with 40 marks |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Name     Correct  Wrong  Unanswered  Score
Anil     10       0      0           40
Bhanu    8        1      1           31
Chitra   4        6      0           10
Deepak   INVALID - expected 10 answers but got 3
Esha     5        4      1           16

Topper: Anil with 40 marks
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program shows how strings can be treated as sequences and compared with an answer key using indexing and loops. Negative marking, invalid input and lower-case answers are all handled, so the evaluation is reliable.

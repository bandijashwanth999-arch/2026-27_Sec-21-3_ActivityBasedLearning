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

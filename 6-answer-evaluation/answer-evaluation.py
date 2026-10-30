key = "ABCDE"
answers = input("Enter 5 answers: ").upper()

correct = 0
wrong = 0
unanswered = 0

for i in range(5):
    if answers[i] == key[i]:
        correct += 1
    elif answers[i] == "X":
        unanswered += 1
    else:
        wrong += 1

marks = correct * 2 - wrong * 0.5

print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Unanswered:", unanswered)
print("Total Marks:", marks)

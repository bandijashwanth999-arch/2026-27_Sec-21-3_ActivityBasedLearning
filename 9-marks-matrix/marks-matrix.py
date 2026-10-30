marks = [
    [80, 75, 90],
    [70, 85, 80],
    [90, 95, 85]
]

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / 3
    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)

for j in range(3):
    total = 0
    for i in range(3):
        total += marks[i][j]

    print("Subject", j + 1, "Average:", total / 3)

employees = [
    ("Rahul", 9, 2),
    ("Arjun", 1, 5),
    ("Ravi", 3, 7)
]

for i in range(len(employees)):
    for j in range(i + 1, len(employees)):
        if employees[i][1] < employees[j][2] and employees[j][1] < employees[i][2]:
            print(employees[i][0], "and", employees[j][0], "have overlapping shifts")

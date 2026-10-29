# Case Study 9: Student Marks Matrix Analysis
# Goal: row/column statistics on a nested list, top performer, weak subjects.

students = ["Anil", "Bhanu", "Chitra", "Deepak", "Esha"]
subjects = ["Python", "Maths", "Physics", "English"]
marks = [
    [78, 65, 70, 82],     # Anil
    [45, 38, 52, 60],     # Bhanu
    [92, 88, 85, 90],     # Chitra
    [56, 42, 48, 70],     # Deepak
    [67, 55, 40, 75],     # Esha
]
LOW_AVERAGE = 60          # a subject average below this is "low"
PASS_MARK = 40            # a mark below this is a failure in that subject

rows = len(marks)
cols = len(subjects)

# ---- Row-wise: total and average of each student ----
print("Student   Total  Average")
best_total = -1
totals = []
for r in range(rows):
    total = 0
    for c in range(cols):
        total = total + marks[r][c]
    totals.append(total)
    print(f"{students[r]:<10}{total:<7}{total / cols:.2f}")
    if total > best_total:
        best_total = total

# ---- Top performer(s): handles ties ----
print()
print("Top performer(s):", end=" ")
for r in range(rows):
    if totals[r] == best_total:
        print(students[r], end=" ")
print("with", best_total, "marks")

# ---- Column-wise: average, highest, lowest of each subject ----
print()
print("Subject   Average  Highest  Lowest")
low_subjects = []
for c in range(cols):
    col_total = 0
    highest = marks[0][c]
    lowest = marks[0][c]
    for r in range(rows):
        value = marks[r][c]
        col_total = col_total + value
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value
    average = col_total / rows
    print(f"{subjects[c]:<10}{average:<9.2f}{highest:<9}{lowest}")
    if average < LOW_AVERAGE:
        low_subjects.append(subjects[c])

print()
print("Subjects with low average (below " + str(LOW_AVERAGE) + "):", ", ".join(low_subjects))

# ---- Individual failures ----
print()
print("Marks below pass mark (" + str(PASS_MARK) + "):")
found = False
for r in range(rows):
    for c in range(cols):
        if marks[r][c] < PASS_MARK:
            print(" ", students[r], "in", subjects[c], "scored", marks[r][c])
            found = True
if not found:
    print("  None")

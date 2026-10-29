# University Scholarship Allocation (Case Study 1)

## 1. Problem Statement
A university offers a limited number of scholarships. Each applicant has aggregate marks, a lowest subject mark, attendance and family income. The system must check every applicant against the eligibility rules, rank the eligible students, and resolve ties using fixed rules.

## 2. Objectives
- Validate each applicant against four criteria (aggregate, subject minimum, attendance, income).
- Report the exact reason(s) for rejection.
- Rank eligible students using a main rule and tie-break rules.
- Award scholarships to the top students within the quota; others go to the waiting list.

## 3. Assumptions
- Aggregate, subject minimum and attendance are percentages (0-100); income is yearly, in rupees.
- Policy: aggregate >= 75, every subject >= 50, attendance >= 75, income <= 3,00,000, quota = 3.
- Ranking: higher aggregate first; tie -> higher attendance; still tied -> lower income.
- Input data is stored in the program (list of tuples) and is assumed to be correct numbers.

## 4. Algorithm
1. Start and store policy values and the applicant list.
2. For each applicant, unpack the tuple and test the four rules; collect reasons for failure.
3. If there are no reasons, add the applicant to the eligible list; otherwise print the reasons.
4. Sort the eligible list with bubble sort using the three ranking rules.
5. Print the rank list; rank <= quota is AWARDED, the rest are WAITING LIST.
6. Stop.

## 5. Pseudocode
```
SET policy values (MIN_AGG, MIN_SUBJECT, MIN_ATT, MAX_INCOME, QUOTA)
CREATE empty list eligible
FOR each applicant IN applicants
    UNPACK name, aggregate, lowest, attendance, income
    CREATE empty list reasons
    IF aggregate < MIN_AGG THEN add reason
    IF lowest < MIN_SUBJECT THEN add reason
    IF attendance < MIN_ATT THEN add reason
    IF income > MAX_INCOME THEN add reason
    IF reasons is empty THEN add applicant to eligible
    ELSE PRINT name and reasons
END FOR
FOR i = 0 TO n-2
    FOR j = 0 TO n-2-i
        IF eligible[j+1] is better than eligible[j] THEN
            (higher aggregate, else higher attendance, else lower income)
            SWAP them
        END IF
    END FOR
END FOR
rank = 1
FOR each student IN eligible
    IF rank <= QUOTA THEN status = AWARDED ELSE status = WAITING LIST
    PRINT rank, details, status
    rank = rank + 1
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 1: University Scholarship Allocation
# Goal: check eligibility, rank eligible students, break ties by rules.

# ---- Policy (change these values to test other policies) ----
MIN_AGGREGATE = 75      # minimum aggregate marks (%)
MIN_SUBJECT = 50        # minimum marks in every subject
MIN_ATTENDANCE = 75     # minimum attendance (%)
MAX_INCOME = 300000     # maximum yearly family income (Rs.)
QUOTA = 3               # number of scholarships available

# Each applicant is a tuple: (name, aggregate, lowest_subject_mark, attendance, income)
applicants = [
    ("Asha", 88, 62, 92, 150000),
    ("Ravi", 82, 55, 85, 200000),
    ("Meena", 88, 60, 92, 120000),
    ("Kiran", 70, 60, 90, 100000),
    ("Sita", 85, 45, 95, 180000),
    ("Arjun", 79, 58, 70, 90000),
    ("Divya", 82, 55, 85, 180000),
    ("Rohit", 91, 70, 96, 350000),
]

eligible = []   # will hold only the students who pass every rule

print("=== ELIGIBILITY CHECK ===")
for student in applicants:
    name, aggregate, lowest, attendance, income = student   # tuple unpacking
    reasons = []                                            # reasons for rejection
    if aggregate < MIN_AGGREGATE:
        reasons.append("aggregate below " + str(MIN_AGGREGATE))
    if lowest < MIN_SUBJECT:
        reasons.append("a subject mark below " + str(MIN_SUBJECT))
    if attendance < MIN_ATTENDANCE:
        reasons.append("attendance below " + str(MIN_ATTENDANCE))
    if income > MAX_INCOME:
        reasons.append("income above " + str(MAX_INCOME))

    if len(reasons) == 0:
        eligible.append(student)
        print(name, ": ELIGIBLE")
    else:
        print(name, ": REJECTED ->", ", ".join(reasons))

# ---- Ranking using bubble sort ----
# Rule 1: higher aggregate first
# Rule 2 (tie): higher attendance first
# Rule 3 (tie): lower income first
n = len(eligible)
for i in range(n - 1):
    for j in range(n - 1 - i):
        a = eligible[j]
        b = eligible[j + 1]
        b_is_better = False
        if b[1] > a[1]:
            b_is_better = True
        elif b[1] == a[1]:
            if b[3] > a[3]:
                b_is_better = True
            elif b[3] == a[3]:
                if b[4] < a[4]:
                    b_is_better = True
        if b_is_better:
            eligible[j], eligible[j + 1] = b, a             # swap

print()
print("=== FINAL RANK LIST ===")
print("Rank  Name    Aggr  Attend  Income   Status")
rank = 1
for student in eligible:
    name, aggregate, lowest, attendance, income = student
    if rank <= QUOTA:
        status = "AWARDED"
    else:
        status = "WAITING LIST"
    print(str(rank).ljust(6) + name.ljust(8) + str(aggregate).ljust(6)
          + str(attendance).ljust(8) + str(income).ljust(9) + status)
    rank += 1
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | All rules satisfied (Asha: 88, 62, 92, 150000) | ELIGIBLE |
| 2 | Aggregate 70 (Kiran) | REJECTED - aggregate below 75 |
| 3 | One subject mark 45 (Sita) | REJECTED - a subject mark below 50 |
| 4 | Attendance 70 (Arjun) | REJECTED - attendance below 75 |
| 5 | Income 350000 (Rohit) | REJECTED - income above 300000 |
| 6 | Meena and Asha: same aggregate and attendance, incomes 120000 and 150000 | Meena ranked above Asha (lower income) |
| 7 | Divya and Ravi: same aggregate and attendance, incomes 180000 and 200000 | Divya ranked above Ravi (lower income) |
| 8 | 4 eligible students, quota 3 | Ranks 1-3 AWARDED, rank 4 WAITING LIST |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
=== ELIGIBILITY CHECK ===
Asha : ELIGIBLE
Ravi : ELIGIBLE
Meena : ELIGIBLE
Kiran : REJECTED -> aggregate below 75
Sita : REJECTED -> a subject mark below 50
Arjun : REJECTED -> attendance below 75
Divya : ELIGIBLE
Rohit : REJECTED -> income above 300000

=== FINAL RANK LIST ===
Rank  Name    Aggr  Attend  Income   Status
1     Meena   88    92      120000   AWARDED
2     Asha    88    92      150000   AWARDED
3     Divya   82    85      180000   AWARDED
4     Ravi    82    85      200000   WAITING LIST
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program evaluates applicants with conditional statements, shows the reason for every rejection, and ranks the eligible students using a bubble sort with three tie-breaking rules. It uses lists, tuples and tuple unpacking from the syllabus. The policy values are stored in variables, so a different policy can be tested by changing one line.

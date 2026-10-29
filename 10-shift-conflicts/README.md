# Tuple-Based Employee Shift Conflict Detection (Case Study 48)

## 1. Problem Statement
Employee shifts are stored as tuples (employee, day, start hour, end hour). The program must find shifts of the same employee on the same day that overlap, and report the employees with conflicting schedules.

## 2. Objectives
- Store records as tuples and use tuple unpacking.
- Validate each shift's times.
- Compare every pair of shifts using the interval overlap condition.
- Report the conflicts and the affected employees.

## 3. Assumptions
- Times use a 24-hour clock with whole hours.
- A valid shift has 0 <= start < end <= 24.
- Two shifts overlap when start1 < end2 and start2 < end1.
- A shift that starts exactly when another ends is not a conflict.
- Only shifts of the same employee on the same day are compared.

## 4. Algorithm
1. Store the shift tuples.
2. Validate each shift; invalid ones are reported and ignored.
3. For every pair (i, j) with j > i, unpack both tuples.
4. If the employee and day are the same and start1 < end2 and start2 < end1, report a conflict and add the employee to the conflict list (once).
5. Print the total number of conflicts and the employees.

## 5. Pseudocode
```
valid_shifts = empty list
FOR each shift IN shifts
    UNPACK emp, day, start, end
    IF start < 0 OR end > 24 OR start >= end THEN PRINT invalid
    ELSE add shift to valid_shifts
END FOR
FOR i = 0 TO n-1
    FOR j = i+1 TO n-1
        UNPACK shift i and shift j
        IF emp1 == emp2 AND day1 == day2 THEN
            IF start1 < end2 AND start2 < end1 THEN
                PRINT conflict
                conflicts = conflicts + 1
                IF emp1 not in conflict_employees THEN add it
            END IF
        END IF
    END FOR
END FOR
PRINT conflicts and conflict_employees
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 10: Tuple-Based Employee Shift Conflict Detection
# Goal: find employees whose shifts on the same day overlap.

# Each shift is a tuple: (employee, day, start_hour, end_hour)  -- 24-hour clock
shifts = [
    ("E101", "Mon", 9, 17),
    ("E102", "Mon", 8, 12),
    ("E101", "Mon", 16, 22),     # overlaps with the first shift
    ("E101", "Tue", 9, 13),
    ("E102", "Mon", 12, 18),     # starts exactly when previous ends -> NOT a conflict
    ("E103", "Wed", 14, 10),     # invalid: end before start
    ("E102", "Tue", 10, 15),
    ("E102", "Tue", 14, 20),     # overlaps
    ("E104", "Thu", 6, 14),
]

# ---- Step 1: validate every shift ----
valid_shifts = []
print("=== VALIDATION ===")
for shift in shifts:
    emp, day, start, end = shift                 # tuple unpacking
    if start < 0 or end > 24 or start >= end:
        print("Invalid shift ignored:", shift)
    else:
        valid_shifts.append(shift)
print("Valid shifts:", len(valid_shifts), "of", len(shifts))

# ---- Step 2: compare every pair of shifts ----
print()
print("=== CONFLICTS ===")
conflict_employees = []
conflicts_found = 0
for i in range(len(valid_shifts)):
    for j in range(i + 1, len(valid_shifts)):
        emp1, day1, start1, end1 = valid_shifts[i]
        emp2, day2, start2, end2 = valid_shifts[j]
        # same employee, same day, and time intervals overlap
        if emp1 == emp2 and day1 == day2:
            if start1 < end2 and start2 < end1:
                print(f"{emp1} on {day1}: {start1}-{end1} overlaps {start2}-{end2}")
                conflicts_found = conflicts_found + 1
                if emp1 not in conflict_employees:
                    conflict_employees.append(emp1)

print()
print("Total conflicts:", conflicts_found)
if conflicts_found > 0:
    print("Employees with conflicts:", ", ".join(conflict_employees))
else:
    print("No conflicts found.")
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | E101 Mon 9-17 and 16-22 | Conflict (overlap 16-17) |
| 2 | E102 Mon 8-12 and 12-18 | No conflict (touching shifts) |
| 3 | E102 Tue 10-15 and 14-20 | Conflict (overlap 14-15) |
| 4 | E103 Wed 14-10 | Invalid shift ignored (end before start) |
| 5 | Different employees on the same day | Never compared, so no conflict |
| 6 | Whole data set | Valid shifts 8 of 9; 2 conflicts; employees E101, E102 |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
=== VALIDATION ===
Invalid shift ignored: ('E103', 'Wed', 14, 10)
Valid shifts: 8 of 9

=== CONFLICTS ===
E101 on Mon: 9-17 overlaps 16-22
E102 on Tue: 10-15 overlaps 14-20

Total conflicts: 2
Employees with conflicts: E101, E102
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program uses tuples to store fixed records and unpacking to read them clearly. The overlap condition start1 < end2 and start2 < end1 correctly handles all cases, including shifts that only touch, and invalid data is filtered out first.

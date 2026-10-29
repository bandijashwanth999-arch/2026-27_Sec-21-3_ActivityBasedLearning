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

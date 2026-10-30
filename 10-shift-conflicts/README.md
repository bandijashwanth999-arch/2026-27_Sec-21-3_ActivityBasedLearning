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

## 5. Conclusion
The program uses tuples to store fixed records and unpacking to read them clearly. The overlap condition start1 < end2 and start2 < end1 correctly handles all cases, including shifts that only touch, and invalid data is filtered out first.

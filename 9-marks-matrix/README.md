# Nested Loop Calendar Generator (Case Study 37)

## 1. Problem Statement
Generate a formatted monthly calendar from the month name, the number of days and the weekday on which the month starts. The weeks must be aligned, and invalid month lengths or weekdays must be rejected.

## 2. Objectives
- Use loops and a column counter to arrange days into weeks.
- Align every day number in a fixed width of 3 characters.
- Validate the number of days and the starting weekday.

## 3. Assumptions
- Starting weekday: 0 = Monday ... 6 = Sunday.
- A valid month has 28 to 31 days.
- The calendar is printed with Monday as the first column.

## 4. Algorithm
1. For each (title, days, start) tuple, validate days (28 to 31) and start (0 to 6).
2. Print the centred title and the header 'Mo Tu We Th Fr Sa Su'.
3. Start the first line with 3 spaces for each empty cell before day 1.
4. For day = 1 to days: add the day in a 3-character cell and increase the column.
5. When the column reaches 7, print the line and start a new week.
6. After the loop, print the last partial week if it is not empty.

## 5. Pseudocode
```
FOR each (title, days, start) IN months
    IF days < 28 OR days > 31 THEN PRINT error; CONTINUE
    IF start < 0 OR start > 6 THEN PRINT error; CONTINUE
    PRINT title (centred)
    PRINT "Mo Tu We Th Fr Sa Su"
    line = 3 spaces * start
    column = start
    FOR day = 1 TO days
        IF day < 10 THEN line = line + " " + day + " "
        ELSE line = line + day + " "
        column = column + 1
        IF column == 7 THEN PRINT line; line = ""; column = 0
    END FOR
    IF line != "" THEN PRINT line
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 8: Nested Loop Calendar Generator
# Goal: print a month calendar from (month name, number of days, starting weekday).
# Starting weekday: 0 = Monday, 1 = Tuesday, ... 6 = Sunday

months = [
    ("October 2026", 31, 3),     # starts on Thursday
    ("February 2026", 28, 6),    # starts on Sunday
    ("April 2026", 30, 2),       # starts on Wednesday
    ("Wrong Month", 32, 1),      # invalid number of days
    ("Wrong Start", 30, 7),      # invalid weekday
]

for title, days, start in months:
    # ---- validation ----
    if days < 28 or days > 31:
        print(title, "-> Invalid: a month must have 28 to 31 days.")
        print()
        continue
    if start < 0 or start > 6:
        print(title, "-> Invalid: starting weekday must be 0 to 6.")
        print()
        continue

    # ---- heading ----
    print(title.center(21))
    print("Mo Tu We Th Fr Sa Su")

    # ---- body ----
    line = "   " * start               # empty cells before day 1
    column = start                     # which weekday column we are in
    for day in range(1, days + 1):
        if day < 10:
            line = line + " " + str(day) + " "
        else:
            line = line + str(day) + " "
        column = column + 1
        if column == 7:                # week finished, print and start next line
            print(line)
            line = ""
            column = 0
    if line != "":                     # print the last (partial) week
        print(line)
    print()
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | October 2026, 31 days, start 3 (Thursday) | Day 1 under 'Th'; last day 31 under 'Sa'; 5 week-lines |
| 2 | February 2026, 28 days, start 6 (Sunday) | Day 1 under 'Su' on its own line; 5 week-lines ending on 28 |
| 3 | April 2026, 30 days, start 2 (Wednesday) | Day 1 under 'We'; last day 30 under 'Th' |
| 4 | 32 days | Invalid: a month must have 28 to 31 days. |
| 5 | Start weekday 7 | Invalid: starting weekday must be 0 to 6. |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
     October 2026    
Mo Tu We Th Fr Sa Su
          1  2  3  4 
 5  6  7  8  9 10 11 
12 13 14 15 16 17 18 
19 20 21 22 23 24 25 
26 27 28 29 30 31 

    February 2026    
Mo Tu We Th Fr Sa Su
                   1 
 2  3  4  5  6  7  8 
 9 10 11 12 13 14 15 
16 17 18 19 20 21 22 
23 24 25 26 27 28 

      April 2026     
Mo Tu We Th Fr Sa Su
       1  2  3  4  5 
 6  7  8  9 10 11 12 
13 14 15 16 17 18 19 
20 21 22 23 24 25 26 
27 28 29 30 

Wrong Month -> Invalid: a month must have 28 to 31 days.

Wrong Start -> Invalid: starting weekday must be 0 to 6.
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program uses a column counter inside a loop to wrap days into weeks, and fixed-width strings to align the output. It validates its inputs, and the same code works for any valid month length and start day.

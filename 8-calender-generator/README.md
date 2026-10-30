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

## 5. Conclusion
The program uses a column counter inside a loop to wrap days into weeks, and fixed-width strings to align the output. It validates its inputs, and the same code works for any valid month length and start day.

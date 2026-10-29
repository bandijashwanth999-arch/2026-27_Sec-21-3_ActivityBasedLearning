# Advanced Numeric Pattern Generator - Hollow Diamond (Case Study 27)

## 1. Problem Statement
Print a hollow diamond pattern made of numbers for a size given by the user. The output must be carefully aligned, and invalid sizes must be rejected with a message.

## 2. Objectives
- Generate a symmetric numeric pattern using nested logic and string repetition.
- Keep the shape aligned using leading spaces and inner gaps.
- Validate the size before printing.

## 3. Assumptions
- Size n must be an integer from 2 to 9, so that every number is a single digit and alignment is not broken.
- Row i prints the number i at the left and right edges; the first and last rows print a single 1.
- Sizes are supplied from a list in the program (can be changed to keyboard input).

## 4. Algorithm
1. For each size n, check 2 <= n <= 9; if not, print an error and go to the next size.
2. Build the list of row numbers: 1, 2, ..., n, n-1, ..., 1.
3. For each row number i, start the line with (n - i) spaces.
4. If i = 1, add just '1'; otherwise add i, then (2i - 3) spaces, then i.
5. Print the line.
6. Print a blank line after each pattern.

## 5. Pseudocode
```
FOR each n IN sizes
    IF n < 2 OR n > 9 THEN
        PRINT "Invalid size"
        CONTINUE
    END IF
    rows = [1..n] followed by [n-1..1]
    FOR each i IN rows
        line = (n - i) spaces
        IF i == 1 THEN line = line + i
        ELSE line = line + i + (2*i - 3) spaces + i
        PRINT line
    END FOR
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 4: Advanced Numeric Pattern Generator (Hollow Numeric Diamond)
# Goal: print a hollow diamond made of numbers, validating the size first.

# Sizes to try. (Replace with: sizes = [int(input("Enter size: "))] to use keyboard input)
sizes = [5, 1, 12, 4, 9]

for n in sizes:
    print("Size =", n)
    # Valid size: 2 to 9 (so that every number is a single digit and the output stays aligned)
    if n < 2 or n > 9:
        print("Invalid size! Enter a value from 2 to 9.")
        print()
        continue

    # rows go 1,2,...,n and then n-1,...,1
    rows = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

    for i in rows:
        line = " " * (n - i)                    # leading spaces for alignment
        if i == 1:
            line = line + str(i)                # top and bottom tip: only one number
        else:
            gap = " " * (2 * i - 3)             # hollow space between the two numbers
            line = line + str(i) + gap + str(i)
        print(line)
    print()
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | n = 5 | Hollow diamond: rows 1 2 3 4 5 4 3 2 1, aligned, 9 lines |
| 2 | n = 4 | Hollow diamond with 7 lines |
| 3 | n = 9 (largest allowed) | 17 lines, widest row '9' and '9' with 13 spaces between |
| 4 | n = 2 (smallest allowed) | 3 lines: 1, then '2 2', then 1 (with alignment spaces) |
| 5 | n = 1 | Invalid size! Enter a value from 2 to 9. |
| 6 | n = 12 | Invalid size! Enter a value from 2 to 9. |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Size = 5
    1
   2 2
  3   3
 4     4
5       5
 4     4
  3   3
   2 2
    1

Size = 1
Invalid size! Enter a value from 2 to 9.

Size = 12
Invalid size! Enter a value from 2 to 9.

Size = 4
   1
  2 2
 3   3
4     4
 3   3
  2 2
   1

Size = 9
        1
       2 2
      3   3
     4     4
    5       5
   6         6
  7           7
 8             8
9               9
 8             8
  7           7
   6         6
    5       5
     4     4
      3   3
       2 2
        1
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program prints a perfectly aligned hollow numeric diamond using loops and string repetition, and it rejects invalid sizes. The key idea is that a symmetric shape can be produced from one loop over the row list 1..n..1, which avoids repeating code for the upper and lower halves.

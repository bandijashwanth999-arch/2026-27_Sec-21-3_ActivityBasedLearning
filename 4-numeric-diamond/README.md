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



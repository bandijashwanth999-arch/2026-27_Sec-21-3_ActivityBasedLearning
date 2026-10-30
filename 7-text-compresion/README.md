# Text Compression Using Character Runs (Case Study 35)

## 1. Problem Statement
Compress a string by replacing each group of consecutive repeated characters with the character and its count (for example, aaabb becomes a3b2). The program must compare the original and encoded lengths, because encoding is sometimes longer than the original.

## 2. Objectives
- Group consecutive equal characters using a loop.
- Build the encoded string using string concatenation and str().
- Compare lengths and say whether compression is beneficial.
- Handle an empty string and runs longer than 9.

## 3. Assumptions
- The text contains letters only (no digits), so the encoded text is unambiguous.
- Upper and lower case are different characters (A and a are not grouped).
- Encoding is 'beneficial' only if the encoded length is strictly smaller than the original.

## 4. Algorithm
1. Take a string text; if it is empty, report and stop for this string.
2. Set count = 1.
3. Compare each character with the previous one: if equal, increase count; if different, append previous character + count to the output and reset count to 1.
4. After the loop, append the last character and its count.
5. Compare lengths and print the result.

## 5. Conclusion
The program implements run-length encoding with a single loop and shows an important point: compression does not always make data smaller. Comparing lengths before accepting the encoded form is the correct design.

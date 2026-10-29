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

## 5. Pseudocode
```
FOR each text IN samples
    IF text is empty THEN PRINT message; CONTINUE
    encoded = ""
    count = 1
    FOR i = 1 TO length(text)-1
        IF text[i] == text[i-1] THEN count = count + 1
        ELSE
            encoded = encoded + text[i-1] + STR(count)
            count = 1
        END IF
    END FOR
    encoded = encoded + text[last] + STR(count)
    IF length(encoded) < length(text) THEN PRINT "useful"
    ELSE PRINT "not beneficial"
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 7: Text Compression Using Character Runs (Run-Length Encoding)
# Goal: replace repeated characters by character + count, e.g. aaab -> a3b1.
# Show whether the encoded text is actually shorter.

samples = ["aaabbbcccd", "abcd", "aaaaaaaaaaaa", "AAaa", "wwwwwbbbw", ""]

for text in samples:
    print("Original :", repr(text), "(length " + str(len(text)) + ")")

    if text == "":
        print("Result   : Empty string - nothing to encode")
        print()
        continue

    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1                       # same character, extend the run
        else:
            encoded = encoded + text[i - 1] + str(count)   # save finished run
            count = 1
    encoded = encoded + text[-1] + str(count)       # save the last run

    print("Encoded  :", encoded, "(length " + str(len(encoded)) + ")")
    if len(encoded) < len(text):
        saved = len(text) - len(encoded)
        print("Result   : Compression is useful, saved", saved, "characters")
    else:
        print("Result   : Encoding NOT beneficial, keep the original text")
    print()
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | aaabbbcccd | a3b3c3d1 (8 < 10), useful, saved 2 |
| 2 | abcd | a1b1c1d1 (8 > 4), NOT beneficial |
| 3 | aaaaaaaaaaaa (12 a's) | a12 (3 < 12), useful, saved 9 |
| 4 | AAaa | A2a2 (4 = 4), NOT beneficial |
| 5 | wwwwwbbbw | w5b3w1 (6 < 9), useful, saved 3 |
| 6 | (empty string) | Empty string - nothing to encode |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Original : 'aaabbbcccd' (length 10)
Encoded  : a3b3c3d1 (length 8)
Result   : Compression is useful, saved 2 characters

Original : 'abcd' (length 4)
Encoded  : a1b1c1d1 (length 8)
Result   : Encoding NOT beneficial, keep the original text

Original : 'aaaaaaaaaaaa' (length 12)
Encoded  : a12 (length 3)
Result   : Compression is useful, saved 9 characters

Original : 'AAaa' (length 4)
Encoded  : A2a2 (length 4)
Result   : Encoding NOT beneficial, keep the original text

Original : 'wwwwwbbbw' (length 9)
Encoded  : w5b3w1 (length 6)
Result   : Compression is useful, saved 3 characters

Original : '' (length 0)
Result   : Empty string - nothing to encode
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program implements run-length encoding with a single loop and shows an important point: compression does not always make data smaller. Comparing lengths before accepting the encoded form is the correct design.

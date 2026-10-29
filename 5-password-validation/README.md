# Password Policy Validation Engine (Case Study 29)

## 1. Problem Statement
Evaluate sample passwords against a policy (length, character categories, repetition, prohibited words) and explain every rule that fails, not just the first one.

## 2. Objectives
- Check passwords against five rules using strings, loops and conditions.
- Collect all failures in a list and report each one.
- Make the check for prohibited words case-insensitive.

## 3. Assumptions
- Minimum length is 8.
- Required: one uppercase letter, one lowercase letter, one digit and one special character from !@#$%^&*.
- The same character may not appear 3 times in a row.
- Prohibited substrings (any letter case): password, 1234, qwerty, admin.

## 4. Algorithm
1. For each password, create an empty list of failures.
2. Check the length.
3. Scan each character and note whether upper, lower, digit and special characters were found.
4. Add a failure for each missing category.
5. Check every 3 neighbouring characters for repetition.
6. Convert the password to lower case and test each prohibited word with 'in'.
7. If the failure list is empty print VALID, otherwise print every failure.

## 5. Pseudocode
```
FOR each pwd IN passwords
    failures = empty list
    IF length(pwd) < 8 THEN add "too short"
    has_upper = has_lower = has_digit = has_special = False
    FOR each ch IN pwd
        IF ch is A-Z THEN has_upper = True
        ELSE IF ch is a-z THEN has_lower = True
        ELSE IF ch is 0-9 THEN has_digit = True
        ELSE IF ch in SPECIAL THEN has_special = True
    END FOR
    ADD a failure for each False flag
    FOR i = 0 TO length-3
        IF pwd[i] == pwd[i+1] == pwd[i+2] THEN add "repeated", BREAK
    END FOR
    FOR each word IN BANNED
        IF word in lower(pwd) THEN add "prohibited text"
    END FOR
    IF failures empty THEN PRINT VALID ELSE PRINT each failure
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 5: Password Policy Validation Engine
# Goal: check passwords against 5 rules and explain every failed rule.

MIN_LENGTH = 8
SPECIAL = "!@#$%^&*"
BANNED = ["password", "1234", "qwerty", "admin"]    # prohibited substrings

passwords = ["Hello@2026", "short1!", "alllowercase123", "MyPassword#9", "Aaa111!!!bC", "qwerty"]

for pwd in passwords:
    failures = []                                   # list of failed rules

    # Rule 1: length
    if len(pwd) < MIN_LENGTH:
        failures.append("Too short: needs at least " + str(MIN_LENGTH) + " characters")

    # Rule 2: character categories
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pwd:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in SPECIAL:
            has_special = True
    if not has_upper:
        failures.append("Missing an uppercase letter")
    if not has_lower:
        failures.append("Missing a lowercase letter")
    if not has_digit:
        failures.append("Missing a digit")
    if not has_special:
        failures.append("Missing a special character (" + SPECIAL + ")")

    # Rule 3: no character repeated 3 times in a row
    for i in range(len(pwd) - 2):
        if pwd[i] == pwd[i + 1] and pwd[i + 1] == pwd[i + 2]:
            failures.append("Same character repeated 3 times: '" + pwd[i] + "'")
            break

    # Rule 4: prohibited words (ignore upper/lower case)
    lowered = pwd.lower()
    for word in BANNED:
        if word in lowered:
            failures.append("Contains prohibited text: '" + word + "'")

    # Result
    if len(failures) == 0:
        print(pwd, "-> VALID")
    else:
        print(pwd, "-> INVALID (" + str(len(failures)) + " problem(s))")
        for f in failures:
            print("    -", f)
    print()
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | Hello@2026 | VALID |
| 2 | short1! | INVALID (2): too short, missing uppercase |
| 3 | alllowercase123 | INVALID (3): missing uppercase, missing special, 'l' repeated 3 times |
| 4 | MyPassword#9 | INVALID (1): contains prohibited text 'password' |
| 5 | Aaa111!!!bC | INVALID (1): '1' repeated 3 times |
| 6 | qwerty | INVALID (5): too short, no uppercase, no digit, no special, contains 'qwerty' |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Hello@2026 -> VALID

short1! -> INVALID (2 problem(s))
    - Too short: needs at least 8 characters
    - Missing an uppercase letter

alllowercase123 -> INVALID (3 problem(s))
    - Missing an uppercase letter
    - Missing a special character (!@#$%^&*)
    - Same character repeated 3 times: 'l'

MyPassword#9 -> INVALID (1 problem(s))
    - Contains prohibited text: 'password'

Aaa111!!!bC -> INVALID (1 problem(s))
    - Same character repeated 3 times: '1'

qwerty -> INVALID (5 problem(s))
    - Too short: needs at least 8 characters
    - Missing an uppercase letter
    - Missing a digit
    - Missing a special character (!@#$%^&*)
    - Contains prohibited text: 'qwerty'
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The engine checks several independent rules and reports every failed one with a clear explanation, which is how real sign-up forms guide users. It uses string indexing, character comparison, loops, membership tests and lists. Since the rules are stored in variables, they can be changed without rewriting the logic.

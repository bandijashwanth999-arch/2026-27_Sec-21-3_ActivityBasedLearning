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

## 5. Conclusion
The engine checks several independent rules and reports every failed one with a clear explanation, which is how real sign-up forms guide users. It uses string indexing, character comparison, loops, membership tests and lists. Since the rules are stored in variables, they can be changed without rewriting the logic.

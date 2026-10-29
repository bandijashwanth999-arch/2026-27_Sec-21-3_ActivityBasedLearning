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

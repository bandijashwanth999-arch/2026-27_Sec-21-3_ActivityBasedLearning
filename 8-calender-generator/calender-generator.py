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

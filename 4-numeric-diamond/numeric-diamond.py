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

days = int(input("Enter number of days: "))
start = int(input("Enter starting weekday (0-6): "))

print("Mon Tue Wed Thu Fri Sat Sun")

for i in range(start):
    print("    ", end="")

for day in range(1, days + 1):
    print("%3d" % day, end=" ")

    if (day + start) % 7 == 0:
        print()

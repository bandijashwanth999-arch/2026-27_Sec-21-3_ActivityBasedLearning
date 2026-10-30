# Case Study 2: Progressive Electricity Billing
units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5

bill = bill + 50

print("Electricity Bill:", bill)

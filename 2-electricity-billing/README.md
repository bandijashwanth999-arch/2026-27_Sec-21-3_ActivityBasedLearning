# Progressive Electricity Billing (Case Study 2)

## 1. Problem Statement
A household's electricity bill depends on slabs: the more units used, the higher the rate per unit. A fixed charge, a surcharge for high consumption and a rebate for low consumption are also applied. Bills of several months must be compared to find unusual increases.

## 2. Objectives
- Calculate slab-wise energy charges for each month.
- Add the fixed charge and surcharge, and subtract the rebate.
- Compare each month with the previous month (percentage change).
- Identify months with an unusual increase.

## 3. Assumptions
- Slabs: first 100 units at Rs.3.00, next 100 at Rs.4.50, next 100 at Rs.6.00, above 300 at Rs.7.50.
- Fixed charge Rs.50 every month.
- Surcharge of 5% of energy charge if units > 300; rebate of Rs.25 if units <= 100.
- An increase of more than 40% over the previous month is called unusual.
- Units are non-negative numbers; there are six months of data.

## 4. Algorithm
1. Store tariff values, month names and units used.
2. For each month, charge the first three slabs one by one using a loop; charge remaining units at the top rate.
3. Calculate surcharge (if units > 300) and rebate (if units <= 100).
4. Total = energy + fixed + surcharge - rebate.
5. For months after the first, find percentage change from the previous total; if it is above 40%, mark UNUSUAL.
6. Print the table and the list of unusual months.

## 5. Pseudocode
```
SET slab sizes, slab rates, TOP_RATE, FIXED, limits
previous_bill = 0
FOR each month i
    units = units_used[i]
    remaining = units
    energy = 0
    FOR k = 0 TO 2
        IF remaining > slab_size[k] THEN used = slab_size[k] ELSE used = remaining
        energy = energy + used * slab_rate[k]
        remaining = remaining - used
    END FOR
    energy = energy + remaining * TOP_RATE
    surcharge = 0 ; rebate = 0
    IF units > 300 THEN surcharge = 5% of energy
    IF units <= 100 THEN rebate = 25
    total = energy + FIXED + surcharge - rebate
    IF i > 0 THEN
        change = (total - previous_bill) / previous_bill * 100
        IF change > 40 THEN mark month as UNUSUAL
    END IF
    PRINT row
    previous_bill = total
END FOR
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
# Case Study 2: Progressive Electricity Billing
# Goal: slab-wise billing, fixed charge, surcharge, rebate, and unusual-increase detection.

# ---- Tariff ----
SLAB_SIZES = [100, 100, 100]        # first 100, next 100, next 100 units
SLAB_RATES = [3.0, 4.5, 6.0]        # Rs. per unit for those slabs
TOP_RATE = 7.5                      # Rs. per unit above 300 units
FIXED_CHARGE = 50                   # Rs. every month
SURCHARGE_LIMIT = 300               # units above which surcharge applies
SURCHARGE_PERCENT = 5               # % of energy charge
REBATE_LIMIT = 100                  # units up to which rebate applies
REBATE_AMOUNT = 25                  # Rs. rebate for low consumers
INCREASE_LIMIT = 40                 # % rise that is called "unusual"

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units_used = [90, 120, 150, 210, 340, 180]

previous_bill = 0
unusual_months = []

print("Month  Units  Energy   Surcharge  Rebate  Total    Change")
for i in range(len(months)):
    units = units_used[i]
    remaining = units
    energy = 0.0

    # charge each slab one by one
    for k in range(3):
        if remaining > SLAB_SIZES[k]:
            used = SLAB_SIZES[k]
        else:
            used = remaining
        energy = energy + used * SLAB_RATES[k]
        remaining = remaining - used
    energy = energy + remaining * TOP_RATE      # units above 300 (if any)

    surcharge = 0.0
    if units > SURCHARGE_LIMIT:
        surcharge = energy * SURCHARGE_PERCENT / 100

    rebate = 0
    if units <= REBATE_LIMIT:
        rebate = REBATE_AMOUNT

    total = energy + FIXED_CHARGE + surcharge - rebate

    # compare with the previous month
    if i == 0:
        change_text = "-"
    else:
        change = (total - previous_bill) / previous_bill * 100
        change_text = f"{change:.1f}%"
        if change > INCREASE_LIMIT:
            change_text = change_text + "  <-- UNUSUAL"
            unusual_months.append(months[i])

    print(f"{months[i]:<7}{units:<7}{energy:<9.2f}{surcharge:<11.2f}{rebate:<8}{total:<9.2f}{change_text}")
    previous_bill = total

print()
if len(unusual_months) > 0:
    print("Months with unusual increase:", ", ".join(unusual_months))
else:
    print("No unusual increase found.")
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | 90 units | Energy 270.00, rebate 25, total 295.00 |
| 2 | 120 units | Energy 390.00, total 440.00, +49.2% UNUSUAL |
| 3 | 150 units | Energy 525.00, total 575.00, +30.7% (normal) |
| 4 | 210 units | Energy 810.00, total 860.00, +49.6% UNUSUAL |
| 5 | 340 units (above 300) | Energy 1650.00, surcharge 82.50, total 1782.50, +107.3% UNUSUAL |
| 6 | 180 units after 340 | Total 710.00, -60.2% (decrease, not flagged) |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Month  Units  Energy   Surcharge  Rebate  Total    Change
Jan    90     270.00   0.00       25      295.00   -
Feb    120    390.00   0.00       0       440.00   49.2%  <-- UNUSUAL
Mar    150    525.00   0.00       0       575.00   30.7%
Apr    210    810.00   0.00       0       860.00   49.6%  <-- UNUSUAL
May    340    1650.00  82.50      0       1782.50  107.3%  <-- UNUSUAL
Jun    180    660.00   0.00       0       710.00   -60.2%

Months with unusual increase: Feb, Apr, May
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program applies a slab-based tariff using a loop, handles fixed charge, surcharge and rebate with conditions, and finds months with unusual increases by comparing with the previous bill. Keeping rates in lists and variables makes the program easy to change when the tariff changes.

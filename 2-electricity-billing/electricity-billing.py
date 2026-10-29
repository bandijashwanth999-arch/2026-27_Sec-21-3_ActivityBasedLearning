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

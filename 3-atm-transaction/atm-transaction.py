# Case Study 3: ATM Transaction Sequence Simulation
# Goal: process deposits/withdrawals, keep balance, reject invalid ones, print summary.

balance = 5000
MIN_BALANCE = 500          # balance that must always remain in the account
WITHDRAW_LIMIT = 10000     # maximum amount in one withdrawal

# Each transaction is a tuple: (type, amount)   D = deposit, W = withdraw
transactions = [
    ("D", 2000),
    ("W", 1000),
    ("W", 6000),     # would leave balance below minimum
    ("W", 15000),    # above single withdrawal limit
    ("D", -500),     # negative amount
    ("T", 100),      # unknown type
    ("W", 5500),
    ("D", 1500),
]

total_deposits = 0
total_withdrawals = 0
accepted = 0
rejected = 0

print("Opening balance:", balance)
print("-" * 50)
number = 1
for kind, amount in transactions:            # tuple unpacking in the loop
    message = ""
    if amount <= 0:
        message = "REJECTED - amount must be positive"
    elif kind == "D":
        balance = balance + amount
        total_deposits = total_deposits + amount
        message = "ACCEPTED - deposited"
    elif kind == "W":
        if amount > WITHDRAW_LIMIT:
            message = "REJECTED - above withdrawal limit"
        elif balance - amount < MIN_BALANCE:
            message = "REJECTED - minimum balance rule"
        else:
            balance = balance - amount
            total_withdrawals = total_withdrawals + amount
            message = "ACCEPTED - withdrawn"
    else:
        message = "REJECTED - unknown transaction type"

    if message.startswith("ACCEPTED"):
        accepted = accepted + 1
    else:
        rejected = rejected + 1

    print(f"{number}. {kind} {amount:>6}  {message:<38} Balance: {balance}")
    number = number + 1

print("-" * 50)
print("=== SUMMARY ===")
print("Accepted transactions :", accepted)
print("Rejected transactions :", rejected)
print("Total deposited       :", total_deposits)
print("Total withdrawn       :", total_withdrawals)
print("Closing balance       :", balance)


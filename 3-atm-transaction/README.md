# ATM Transaction Sequence Simulation (Case Study 13)

## 1. Problem Statement
Simulate an ATM account that receives a sequence of deposits and withdrawals. The program must keep the balance, enforce a withdrawal limit and a minimum balance, reject invalid transactions, and print a summary.

## 2. Objectives
- Process a list of transactions one by one.
- Update the simulated balance only for valid transactions.
- Reject invalid ones with a clear reason.
- Print accepted/rejected counts, totals and the closing balance.

## 3. Assumptions
- Opening balance is Rs.5000.
- Transaction types: D (deposit), W (withdrawal); anything else is invalid.
- Maximum Rs.10000 per withdrawal; Rs.500 must always remain in the account.
- Amounts must be positive.
- Transactions are stored as tuples (type, amount).

## 4. Algorithm
1. Set the opening balance and the limits.
2. For each transaction, unpack type and amount.
3. If amount <= 0, reject.
4. If type is D, add to the balance.
5. If type is W, reject if above the limit or if balance would fall below the minimum; otherwise subtract.
6. Any other type is rejected.
7. Count accepted/rejected and update totals; print each result.
8. After the loop, print the summary.

## 5. Pseudocode
```
balance = 5000
FOR each (kind, amount) IN transactions
    IF amount <= 0 THEN reject
    ELSE IF kind == "D" THEN balance = balance + amount, accept
    ELSE IF kind == "W" THEN
        IF amount > WITHDRAW_LIMIT THEN reject
        ELSE IF balance - amount < MIN_BALANCE THEN reject
        ELSE balance = balance - amount, accept
    ELSE reject (unknown type)
    UPDATE accepted / rejected counters
    PRINT result and balance
END FOR
PRINT summary
```

## 6. Python Source Code
File: [`program.py`](program.py)

```python
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
```

## 7. Test Cases
| # | Input / Scenario | Expected Output |
|---|---|---|
| 1 | D 2000 | ACCEPTED, balance 7000 |
| 2 | W 1000 | ACCEPTED, balance 6000 |
| 3 | W 6000 | REJECTED - minimum balance rule |
| 4 | W 15000 | REJECTED - above withdrawal limit |
| 5 | D -500 | REJECTED - amount must be positive |
| 6 | T 100 | REJECTED - unknown transaction type |
| 7 | W 5500 | ACCEPTED, balance 500 (exactly the minimum) |
| 8 | Summary of the above | Accepted 4, Rejected 4, deposited 3500, withdrawn 6500, closing balance 2000 |

## 8. Output
Text output from running the program (also saved in [`output.txt`](output.txt)).

```text
Opening balance: 5000
--------------------------------------------------
1. D   2000  ACCEPTED - deposited                   Balance: 7000
2. W   1000  ACCEPTED - withdrawn                   Balance: 6000
3. W   6000  REJECTED - minimum balance rule        Balance: 6000
4. W  15000  REJECTED - above withdrawal limit      Balance: 6000
5. D   -500  REJECTED - amount must be positive     Balance: 6000
6. T    100  REJECTED - unknown transaction type    Balance: 6000
7. W   5500  ACCEPTED - withdrawn                   Balance: 500
8. D   1500  ACCEPTED - deposited                   Balance: 2000
--------------------------------------------------
=== SUMMARY ===
Accepted transactions : 4
Rejected transactions : 4
Total deposited       : 3500
Total withdrawn       : 6500
Closing balance       : 2000
```

**Output screenshot:** run `python program.py` and save a screenshot as `screenshots/output.png`, then uncomment the next line.

<!-- ![Output screenshot](screenshots/output.png) -->

## 9. Conclusion
The program simulates a real ATM account using a loop, conditions and tuple unpacking. Every transaction is validated before it changes the balance, so the balance never becomes invalid, and the summary gives a complete audit of the run.

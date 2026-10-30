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
   
## 5. Conclusion
The program simulates a real ATM account using a loop, conditions and tuple unpacking. Every transaction is validated before it changes the balance, so the balance never becomes invalid, and the summary gives a complete audit of the run.

balance = 5000

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

   choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        balance += amount

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance and amount <= 10000:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or limit exceeded")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        break

    else:
        print("Invalid choice")

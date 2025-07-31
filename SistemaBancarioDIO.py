menu = """

[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

> """

balance = 0
limit = 500
statement = ""
withdrawLimit = 3
depositCount = 0
withdrawCount = 0

while True:
    option = input(menu).strip()
    if option == "1":
        amount = float(input("Enter the deposit amount: "))
        if amount > 0:
            balance += amount
            depositCount += 1
            statement += f"Deposited: R$ {amount:.2f}\n"
            print(f"Successfully deposited R$ {amount:.2f}")
        else:
            print("Deposit a valid amount.")

    elif option == "2":
        if withdrawCount >= withdrawLimit:
            print("Withdrawal limit reached.")
            continue
        if balance <= 0:
            print("Insufficient funds.")
            continue

        amount = float(input("Enter the withdrawal amount: "))
        if amount > limit:
            print(f"Maximum withdrawal amount reached.")
        elif amount > balance:
            print(f"Insufficient funds. Your balance is R$ {balance:.2f}")
        elif amount <= 0:
            print("Withdraw a valid amount.")
        else:
            balance -= amount
            withdrawCount += 1
            statement += f"Withdrawal: R$ {amount:.2f}\n"
            print(f"Successfully withdrew: R$ {amount:.2f}")

    elif option == "3":
        print("\n|||||||||||| STATEMENT ||||||||||||")
        if not statement:
            print("No transactions yet.")
        else:
            print(statement.strip())

        print(f"\nCurrent balance: R$ {balance:.2f}")
        print(f"Deposits made: {depositCount} times")
        print(f"Withdrawals made: {withdrawCount} times")
        print("|||||||||||||||||||||||||||||||||||\n")
    elif option == "4":
        print("Thanks for using our service!")
        break

    else: 
        print("Select a valid option between 1 and 4!")

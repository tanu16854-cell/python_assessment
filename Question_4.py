# Q4: Banking system

balance = 0

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = float(input("Enter deposit amount: "))
        balance += amt
        print("Deposited Successfully")

    elif choice == 2:
        amt = float(input("Enter withdraw amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdraw Successful")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Exiting system...")
        break

    else:
        print("Invalid Choice")
        
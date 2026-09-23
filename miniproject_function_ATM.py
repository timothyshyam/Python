balance = 0
while True:
    print("ATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        credit_amount = float(input("Enter amount to credit: "))
        if credit_amount <= 0:
            print("Please enter a positive amount.")
        else:
            balance += credit_amount
            print(f"${credit_amount} credited to your account.")
    elif choice == '2':
        debit_amount = float(input("Enter amount to debit: "))
        if debit_amount<= 0:
            print("Please enter a positive amount.")
        elif debit_amount> balance:
            print("Insufficient balance.")
        else:
            balance -= debit_amount
            print(f"${debit_amount} debited from your account.")
    elif choice == '3':
        print(f"Your current balance is: ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

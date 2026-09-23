class ATM():
    def __init__(self,bankname,balance,accname):
        self.bankname = bankname
        self.balance = balance
        self.accname = accname
    def credit(self,):
        credit_amount = int(input("enter amount to be credited:"))
        if credit_amount<=0:
            print("enter an positive amount.")
        else :
            self.balance += credit_amount
            print(f"${credit_amount} amount has credited to your {self.accname} {self.bankname}")
            print(f"total balance is {self.balance}")
    def debit(self,):
        debit_amount = int(input("enter amount to be debited:"))
        if debit_amount<=0:
            print("enter a positive amount.")
        elif debit_amount>self.balance:
            print("insufficient funds.")
        else:
            self.balance-=debit_amount
            print(f"${debit_amount} has been debited from {self.accname}")
            print(f"total balance is {self.balance}")
    def total_balance(self,):
        print(f"your current total savings : {self.balance}")
    def main(self,):
        while True:
            print("\nATM Functions.")
            print("1.credit.")
            print("2.debit")
            print("3.balance")
            print("4.exit")

            choice = int(input("enter the function you want proceed (1-4):"))
            
            if choice ==1:
                self.credit()
            elif choice == 2:
                self.debit()
            elif choice ==3:
                self.total_balance()
            elif choice ==4:
                print("Thanks for chosing our ATM.Good bye!")
                break
            else:
                print("enter an valid option (1-4).")
bank = ATM("sbi",1000,"shyam")
bank.main()
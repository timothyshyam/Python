class ATM_1():
    def __init__(self,balance,bankname,acc_num):
        self.balance = balance
        self.bankname = bankname
        self.acc_num = acc_num
    def credit(self):
        credit_amount = int(input("enter amount to credit:"))
        if credit_amount<=0:
            print ("enter an positive value.")
        else:
            self.balance+=credit_amount
            print(f"${credit_amount} has been credited to your {self.bankname}_{self.acc_num}")
            print(f"total amount in your {self.bankname}_{self.acc_num} : {self.balance}")
    def debit(self):
        debit_amount = int(input("enter amount to debit:"))
        if debit_amount <=0:
             return ("enter an positive value.")
        elif debit_amount>self.balance:
            print("insufficient funds.")
        else:
            self.balance-=debit_amount
            print(f"${debit_amount} amount has been debited from your {self.bankname} {self.acc_num}")
            print(f"total amount in your {self.bankname}_{self.acc_num} : {self.balance}")
class ATM_2(ATM_1):
    def balance_enquiry(self):
        print(f"${self.balance} is your total account balance.")
    def exit(self):
        print("Thank You, for choosing our ATM. Good Bye!")
class ATM_MENU(ATM_2):
    def atm_menu(self):
        print("1.credit")
        print("2.debit")
        print("3.balance enquiry")
        print("4.exit")

ATM = ATM_MENU(1000,"sbi",1234)
while True:
    ATM.atm_menu()

    choice = int(input("enter a choice(1-4):"))

    if choice==1:
        ATM.credit()
    elif choice==2:
        ATM.debit()
    elif choice==3:
        ATM.balance_enquiry()
    elif choice==4:
        ATM.exit()
        break
    else:
        print("enter an valid choice(1-4).")


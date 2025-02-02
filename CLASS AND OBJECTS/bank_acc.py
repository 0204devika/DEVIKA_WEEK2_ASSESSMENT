class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"deposited successfully, amount available: {self.balance}",)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"withdrawn successfully, amount available: {self.balance}")
bal=float(input("enter the balance:"))
account=BankAccount(bal)
account.deposit(1000)
account.withdraw(2000)
    

    
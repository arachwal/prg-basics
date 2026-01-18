class BankAccount:
    def __init__(self,number):
        self.number=number
        self.balance=0.0

    def showBalance(self):
        print(f"ur balance: {self.balance:.2f}")

    def deposit(self,depo):
        self.balance+=depo

    def withdraw(self,withdrawal):
        if withdrawal>self.balance:
            print('you aint got no funds for that lil bro')
        else:
            self.balance=self.balance-withdrawal


account=BankAccount('11 1111 1111 1111 1111 1111 1111')
account.showBalance()
account.deposit(float(input("how much do you want to deposit: ")))
account.showBalance()
account.withdraw(float(input("how much do you want to withdraw: ")))
account.showBalance()
account.withdraw(float(input("how much do you want to withdraw: ")))
account.showBalance()
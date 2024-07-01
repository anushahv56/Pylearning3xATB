class Bank_Account:
    def __init__(self):
        self.balance=0
        self.__private_var=10
    def public_fn(self):
        print(self.__private_var)
    def deposit(self,amount):
        self.balance=+amount
    def withdraw(self,amount):
        self.balance=-amount
    def show_balance(self):
        print("show balance",self.balance)
sbi=Bank_Account()
print(sbi.balance)
sbi.deposit(100)
print(sbi.balance)
sbi.show_balance()
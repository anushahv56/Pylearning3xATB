class Bank_Account:
    def __init__(self):
        self.balance=0
        self.__private_var=10
    def public_fn(self):
        print(self.__private_var)
    def deposit(self,amount):
        self.balance=+amount
    def __withdraw(self,amount):
        self.balance=-amount
    def __show_balance(self):
        print("show balance",self.balance)
    def authentication(self,flag):
        if flag:
            self.__show_balance()
        else:
            print("not allowed")
    def if_ur_authenticate(self,auth):
        if auth:
            self.__withdraw()
        else:
            print("not allowed")
sbi=Bank_Account()
sbi.deposit(100)
secrete_pass=input("enter the pin")
if secrete_pass==123:
    sbi.if_ur_authenticate(True)
else:
    print("not allowed")


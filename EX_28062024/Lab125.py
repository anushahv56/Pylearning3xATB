class VMOLoginpage:
    email=None
    password=None

    def __init__(self,email,password):
        self.email=email
        self.password=password
    def login_confirm(self):
        if self.password=="Pass123":
            print("Allowed")
        else:
            print("not allowed")
email=input("enter the email")
password=input("enter the password")
amit=VMOLoginpage(email, password)
amit.login_confirm()


vasuda=VMOLoginpage("amit@gmail.com","Pass123")
vasuda.login_confirm()
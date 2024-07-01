class VMOlogin:
    def __init__(self,email,password,name):
        self.__email=email
        self.__password=password
        self.name=name
    def login_information(self):
        if self.__email=="pramod@gmail.com" and self.__password==123:
            print("allowed")
        else:
            print("not allowed")
pramod=VMOlogin("pramod@gmail.com",123,"pramod")
pramod.login_information()
print(pramod.name)
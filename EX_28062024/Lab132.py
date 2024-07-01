class Password:
    def __init__(self,password):
        self.__password=password
    def get_password(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("wrong password")
    def set_password(self,password):
        if len(password)>10:
            self.__password=password
            print(self.__password)
        else:
            print("weak pass")
pwd=Password("Hacker123")
pwd.get_password(True)
pwd.set_password("asasasasasa")

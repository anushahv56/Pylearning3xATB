class Car:
    def __init__(self):
        self.public_var="public"
        self._protectedvar="protected"
        self.__privatevar="private var"
    def __private_method(self):
        print("private")
    def public_method(self):
        if self.__privatevar==123:
            print("ia m private var 123")
        print("public")
    def _proted_method(self):
        print("protected")





amit=Car()
amit.public_var
amit.public_method()


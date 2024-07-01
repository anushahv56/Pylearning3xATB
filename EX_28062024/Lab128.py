class my_class:
    def __init__(self):
        print(" ia  m called when obj created")
    def public_method(self):
        print("public function")
    def __private_fun(self):
        print("private fun")
    def public_fn_private(self):
        self.__private_fun()
a=my_class
a.public_method()
a.public_fn_private()



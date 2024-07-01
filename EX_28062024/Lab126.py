#Encapusalation
#wrapping,hidding of data
#Bind the data variable with methods
#methods--Def function within the class
#wrapping or binding the data variables
class Car:
    name=None
    password=123
    def __init__(self):
        print("i am called when object created")
    def change_password(self):
        self.password=345
xuv=Car()
xuv.password=333
xuv.change_password()
print(xuv.password)



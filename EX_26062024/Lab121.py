class Student:
    def __init__(self):
        self.name=input("enter the name")
        self.age=input("enter the age")
    def display(self):
        print("display name",self.name,self.age)
        print(f'{self.name} and age is {self.age}')
s1=Student()
s1.display()
# functions:block of code-which can be executed or reused
# Built in functions present in builtin.py files
# user defined function
# They can return something
# they are not returning anything-->non return
# They have parameters/arguments
# they dont have parameters/arguments


# def say_hello(): #no return type no parameter
#     print("hello")
# say_hello()
#
# def say_hello(name): #no return type with aparameter/argumnet
#     print("hello",name)
# say_hello("Anusha")

def say_hello_defult(name="pramod"):  # no return type with default arg
    print("hello", name)


say_hello_defult()
say_hello_defult("sachin")
say_hello_defult(name="deeksha")


def sum(a, b):
    return a + b


result = sum(2, 3)
print(result)
result = sum(a=2, b=4)
print(result)

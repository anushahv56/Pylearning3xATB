#Decorator
#it is essentially a function taking another function as argument
#and return new function
def my_decorator(func):
    def wrapper():
        print("starting")
        print("*******")
        func()
        print("ending")
        print("*******")
    return wrapper()
@my_decorator
def say_hello():
    print("say hello")


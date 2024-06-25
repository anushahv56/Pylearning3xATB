def decorator1(fun):
    def wrapper():
        print("decorator1")
        fun()

    return wrapper
def decorator2(fun):
    def wrapper():
        print("decorator2")
        fun()

    return wrapper
@decorator1
@decorator2
def say_hello():
    print("say hello")
say_hello()
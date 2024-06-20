number=[1,2,3]
def do_something(number):
    number.append(4)
    number[1]=100
    return number
l=do_something(number)
print(l)
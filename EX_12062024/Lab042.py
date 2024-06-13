#problem max between 3 numbers
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
if (num1>num2) and (num1>num3):
    print(num1,"is max")
elif (num2>num1) and (num2>num3):
    print(num2,"is max")
else:
    print(num3,"is max")
#cntrl+/-->for commenting multiple line
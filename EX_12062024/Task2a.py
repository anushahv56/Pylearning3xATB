# Fibonacci series and Factorial
num=int(input("enter the number"))
factorial=1
if num<0:
    print("factorial doesnot exist")
elif num==0:
    print("factorial is one")
else:
    for i in range(1,num+1):
        factorial=factorial*1
    print("factorial of", num,"is",factorial)

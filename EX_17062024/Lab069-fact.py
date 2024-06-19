#factorial
n=-1
factorial=1
if n==0:
    print("factorail is 1")
elif n>0:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)
else:
    print("not valid num")



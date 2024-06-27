#RECURSION
#it is programing technique where function  call itself to resolve the issue.
#key concept
#1.Base case
#2.recursive case


#Factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n *factorial(n-1)
f=factorial(5)
print(f)
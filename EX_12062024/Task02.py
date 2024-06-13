#task1 1. Leap Year Checker:
year=int(input("enter the year"))
if (year%400==0) and (year%100==0):
    print("it is leap year")
elif(year%4==0) and (year%100!=0):
    print("it is a leap year")
else:
    print("it is not leap year")

#Triangle Classifier:
side1=int(input("enter the length of side1"))
side2=int(input("enter the length of side2"))
side3=int(input("enter the length of side3"))
if side1==side2==side3:
    print("Triangle is equilateral ")
elif (side1==side2) or (side2==side3):
    print("Triangle is isosceles ")
else:
    print("It is scalene ")
#Polymorphism
#it allow object of different class
# to treated as object of common super class
#Pramod  -->husband,mentor,child

#Method overriding
class shape:
    def area(self):
        print("area of shape")
class Rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius *self.radius


shape1=Rectangle(4,3)

print(shape1.area())

shape2=Circle(2)
print(shape2.area())
shape3=shape()
shape3.area()
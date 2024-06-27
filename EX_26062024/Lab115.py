class Dog:
    name=None
    def sleep(self):
        print("sleeping")
        #constructor:use to intialize the value of the instance variables
    def eat(self,name):
        print("eat")
Dog1=Dog()
print(Dog1.name)
Dog1.name="chow"
print(Dog1.name)
Dog1.sleep()
print("-------")
Dog2=Dog()
print(Dog2.name)
Dog2.name="chow2"
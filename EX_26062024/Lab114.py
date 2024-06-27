class Person:
    # Attributes
    name = None
    age = None
    id = None
    phone_num = None

    # Behaviours
    def talk(self): #no arg no return
        print("I can talk")

    def another(self):
        print("I am another method")

    def sleep(self,name): #1 arg 
        print("I am method")
        print("Sleep", self.name)

    def walk(self):
        return "I am walking"

# ObjectRef=object()-->classname()
surya = Person()
surya.name = "Surya Prakash"
surya.talk()
surya.sleep()
surya.another()
surya.walk()
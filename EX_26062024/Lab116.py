class Dog:
    name=None
    id=None
    def __init__(self,name,id):
        self.name=name
        self.id=id


    #__ private in nature
    def sleep(self):
        print("Sleeping",self.name)
Dog1=Dog("chow",1)
Dog1.sleep()
Dog2=Dog("mow",2)
Dog2.sleep()
print(f'{Dog1.name} has id{Dog1.id}')
print(f'{Dog2.name} has id{Dog2.id}')

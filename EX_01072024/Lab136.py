#Hierachical
#one parent--Multiple class
class parent:
    def BHK1(self):
        print("1 bhk")
class pramod(parent):
    def BHK2(self):
        print("2 bhk")
class amit(parent):
    def BHK3(self):
        print("3 bhk")
class lucky(parent):
    def no_house(self):
        print("No house")

pramod_obj=pramod()
pramod_obj.BHK1()
pramod_obj.BHK2()

amit_obj=amit()
amit_obj.BHK1()
amit_obj.BHK2()

lucky_obj=lucky()
lucky_obj.BHK1()
lucky_obj.no_house()

parent_obj=parent()
parent_obj.BHK1()
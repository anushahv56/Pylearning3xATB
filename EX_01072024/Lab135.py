class parent:
    gold="2kg"
    def BHK2(self):
        print("2BHK flat")
class child(parent):


    def BHK3(self):
        print("3BHK flat")

child_object=child()
print(child_object.gold)
child_object.BHK3()
child_object.BHK2()
parent_object=parent()
parent_object.BHK2()
parent_object.gold
#Inheritance-Acquire attribute &Behaviour
#Datamember and methods
#concept in OOPS that allowas one class(child class)to
# inherite Data members and methods from another class(parent class)

#Type of Inheritance
#single
#multiple
#Multilevel
#Hybrid
#Hierachical
class Grandparent:
    key="abc"
    def grandparent_method(self):
        return "grand parent methiod"
class father(Grandparent):

    def father_method(self):
        return "father method"

parent=father()
print(parent.father_method())
print(parent.key)
print(parent.grandparent_method())

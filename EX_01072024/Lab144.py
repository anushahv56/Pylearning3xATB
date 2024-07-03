class Father:
    def home(self):
        print("1BHK")
class son(Father):
    def home(self):
        super().home()
        print("3BHK")
pramod=son()
pramod.home()

#super is used to call my parent function

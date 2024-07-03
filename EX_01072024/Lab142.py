class gf:
    def car(self):
        print("gf methood")
class F(gf):
    def car(self):
        print("f methood")
class S(F):
    def car(self):
        print("S methood")

s_obj=S()
s_obj.car()

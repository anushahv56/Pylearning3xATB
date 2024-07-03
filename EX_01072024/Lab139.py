class A:
    def Amethod(self):
        print("A")
class B:
    def Amethod(self):
        print("B")
class C(B,A): #mrthod Resolution, which one is first attribute it will call first
    pass
c=C()
c.Amethod()
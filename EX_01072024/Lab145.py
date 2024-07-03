#Method overloading is not supported in python
class Mathutil(object):
    def add(self,a,b,c):
        return a+b+c
math=Mathutil()
op0=math.add(1)
print(op0)

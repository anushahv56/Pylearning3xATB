class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
op=Calc(2,3)
output=op.sum()
print(output)

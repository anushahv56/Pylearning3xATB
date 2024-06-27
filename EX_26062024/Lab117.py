class Calc:
    def sum_c(self,a,b):
        return a+b
    def diff_c(self,a,b):
        return a-b
    def mult_c(self,a,b):
        return a*b
    def mod_c(self,a,b):
        return a%b
obj_ref=Calc()
op=obj_ref.sum_c(a=2,b=3)
print(op)


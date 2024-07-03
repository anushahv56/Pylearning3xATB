from abc import ABC,abstractmethod
class Father:
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def loan(self):
        pass
class son(Father):
    def loan(self):
        return "loan cleared"
pramod=son("PPP")
print(pramod.loan())
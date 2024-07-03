from abc import ABC, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("enrolled")





class student(PyATB):
    def payfee(self):
        print("paid")


shubam = student()
shubam.payfee()
shubam.enrolled()
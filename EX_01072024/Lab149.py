from abc import ABC,abstractmethod
class ATB(ABC):
    @abstractmethod
    def task1(self):
        pass
    @abstractmethod
    def task2(self):
        pass
class Amit(ATB):
    def task1(self):
        return "task1"
    def task2(self):
        return "task2"
amit=Amit()
print(amit.task1())
print(amit.task2())
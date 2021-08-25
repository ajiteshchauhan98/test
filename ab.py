from abc import ABCMeta,abstractmethod

class Test(metaclass=ABCMeta):
    @abstractmethod
    def sample(self): pass
    @staticmethod
    def sample2() : print("hh")
Test().sample2()

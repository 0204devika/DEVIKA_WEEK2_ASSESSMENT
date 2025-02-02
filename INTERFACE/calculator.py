from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    def subtract(self,a,b):
        pass
    def multiply(self,a,b):
        pass
    def divide(self,a,b):
        pass
class BasicCalculator(ICalculator):
    def add(self,a,b):
        print("sum is:", a+b)
    def subtract(self,a,b):
        print("difference is:", a-b)
    def multiply(self,a,b):
        print("multiplication is:", a*b)
    def divide(self,a,b):
        print("division is:", a/b)
b=BasicCalculator()
b.add(10,10)
b.subtract(100,1)
b.multiply(12,16)
b.divide(250,25)

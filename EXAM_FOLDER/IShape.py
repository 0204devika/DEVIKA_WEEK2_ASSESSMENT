from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def cal_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def cal_area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def cal_area(self):
        return 3.14*self.r*self.r
r=Rectangle(4,5)
print(r.cal_area())
c=Circle(10)
print(c.cal_area())
        
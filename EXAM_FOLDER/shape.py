class Shape:
    def area(self):
        pass
    from abc import ABC, abstractmethod
class Square(Shape):
    def __init__(self, side):
        self.side=side
    def area(self):
        return self.side*self.side
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height
s=Square(5)
t=Triangle(7,8)
print(s.area())
print(t.area())

        
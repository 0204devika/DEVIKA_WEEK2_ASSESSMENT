#•	10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
class MobileDevice(Electronics):
    def __init__(self,brand,price,color):
        super().__init__(brand,price)
        self.color=color
class SmartPhone(MobileDevice):
    def __init__(self,brand,price,color,size):
        super().__init__(brand,price,color)
        self.size=size
    def disp(self):
        print(f"Brand is {self.brand} and price is {self.price} and size is {self.size}")
s=SmartPhone("Moto",25000,"grey","4x5")
s.disp()
    
        
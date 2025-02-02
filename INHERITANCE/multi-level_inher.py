class Vehicle:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
class Car(Vehicle):
    def __init__(self,brand,color,year):
        super().__init__(brand,color)
        self.year=year
class Bike(Vehicle):
    def __init__(self,brand,color,mileage):
        super().__init__(brand,color)
        self.mileage=mileage
class ElectricCar(Car):
    def __init__(self,brand,color,year,range):
        super().__init__(brand,color,year)
        self.range=range
e=ElectricCar("Activa","white",2018,200)
print("Brand:",e.brand, "Color:",e.color, "Year:",e.year, "Range:",e.range)



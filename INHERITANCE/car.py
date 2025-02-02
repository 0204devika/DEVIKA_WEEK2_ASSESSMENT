class Airplane:
    def move(self):
        return "Airplane is flying"
class Car:
    def move(self):
        return "Car is moving on the ground"
class FlyingCar(Airplane,Car):
    def move(self):
        return Airplane.move(self) + " and " + Car.move(self)
f=FlyingCar()
print(f.move()) 
    
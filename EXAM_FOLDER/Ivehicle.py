from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("car engine started")
    def stop_engine(self):
        print("car engine stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("bike engine started")
    def stop_engine(self):
        print("bike engine stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("truck engine started")
    def stop_engine(self):
        print("truck engine stopped")
c=Car()
b=Bike()
t=Truck()
# Test the interface
c.start_engine()
c.stop_engine()
b.start_engine()
b.stop_engine()
t.start_engine()
t.stop_engine()
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self) -> str:
        raise NotImplementedError

class Car(Vehicle):
    def move(self)->str:
        return 'car is moving'


class Truck(Vehicle):
    def move(self)->str:
        return 'truck is moving'

class Motorcycle(Vehicle):
    def move(self)->str:
        return 'motorcycle is moving'

class VehicleFactory(ABC):

    @abstractmethod
    def create_vehicle(self)->Vehicle:
        raise NotImplementedError

class CarFactory(VehicleFactory):

    def create_vehicle(self)->Vehicle:
        return Car()

class TruckFactory(VehicleFactory):

    def create_vehicle(self)->Vehicle:
        return Truck()

class MotorcycleFactory(VehicleFactory):

    def create_vehicle(self)->Vehicle:
        return Motorcycle()

def get_vehicle_factory(vehicle_type:str)->VehicleFactory:
    factories = {
        "car":CarFactory,
        "truck":TruckFactory,
        "motorcycle":MotorcycleFactory
    }

    if vehicle_type not in factories.keys():
        raise ValueError("Invalid vehicle type")
    
    return factories[vehicle_type]()

if __name__ == "__main__":
    vehicle1 = get_vehicle_factory("car").create_vehicle()
    print(vehicle1.move())
    
    vehicle2 = get_vehicle_factory("truck").create_vehicle()
    print(vehicle2.move())

    vehicle3 = get_vehicle_factory("motorcycle").create_vehicle()
    print(vehicle3.move())
    
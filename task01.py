from abc import ABC, abstractmethod


# Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass


# Клас Car успадковує Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Двигун запущено")


# Клас Motorcycle успадковує Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.spec} Spec): Мотор заведено")


# Абстрактний клас фабрики
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


# Фабрика для транспортних засобів США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


# Фабрика для транспортних засобів ЄС
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


# Використання фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("BMW", "R1250")
vehicle2.start_engine()

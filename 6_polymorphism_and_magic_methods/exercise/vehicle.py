from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        if type(self) == Car:
            burned_fuel = (self.fuel_consumption + Car.SUMMER_INCREMENT) * distance
        else:
            burned_fuel = (self.fuel_consumption + Truck.SUMMER_INCREMENT) * distance

        if self.fuel_quantity >= burned_fuel:
            self.fuel_quantity -= burned_fuel

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_INCREMENT = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)

    def drive(self, distance):
        Vehicle.drive(self, distance)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_INCREMENT = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        Vehicle.__init__(self, fuel_quantity, fuel_consumption)

    def drive(self, distance):
        Vehicle.drive(self, distance)

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel



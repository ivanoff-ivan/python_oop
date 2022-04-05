from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, available_seats, fuel_tank, fuel_consumption, fuel):
        Vehicle.__init__(self, available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self.__fuel = fuel

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        if value >= self.fuel_tank:
            self.__fuel = self.fuel_tank
        else:
            self.__fuel = value

    def drive(self, distance):
        if self.__fuel >= self.fuel_consumption * distance:
            self.__fuel -= self.fuel_consumption * distance
            return "We've enjoyed the travel!"

    def refuel(self, liters):
        if self.__fuel + liters <= self.fuel_tank:
            self.__fuel += liters
        return CapacityMixin.get_capacity(self.fuel_tank, self.fuel_tank - self.__fuel)



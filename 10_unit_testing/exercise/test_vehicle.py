from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 0.9):
            self.fuel_quantity -= distance * (self.fuel_consumption + 0.9)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 1.6):
            self.fuel_quantity -= distance * (self.fuel_consumption + 1.6)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


import unittest


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(200, 3)

    def test_driveMethod_whenFuelQuantityIsEnough_shouldDecreaseFuelQuantity(self):
        self.car.drive(40)
        result = self.car.fuel_quantity
        expected_result = 44
        self.assertEqual(expected_result, result)

    def test_refuelMethod_shouldIncreaseFuel(self):
        self.car.refuel(100)
        result = self.car.fuel_quantity
        expected_result = 300
        self.assertEqual(expected_result, result)


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(200, 3)

    def test_driveMethod_whenFuelQuantityIsEnough_shouldDecreaseFuelQuanity(self):
        self.truck.drive(40)
        result = self.truck.fuel_quantity
        expected_result = 16
        self.assertEqual(expected_result, result)

    def test_refuelMethod_shouldIncreaseFuel(self):
        self.truck.refuel(100)
        result = self.truck.fuel_quantity
        expected_result = 295
        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()
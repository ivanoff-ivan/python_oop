from project.motorcycle import Motorcycle
from project.vehicle import Vehicle


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

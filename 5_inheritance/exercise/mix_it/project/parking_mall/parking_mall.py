from project.capacity_mixin import CapacityMixin


class ParkingMall(CapacityMixin):
    def __init__(self, parking_lots):
        self.parking_lots = parking_lots

    def check_availability(self):
        try:
            available_loots = CapacityMixin.get_capacity(self.parking_lots, 1)
            if available_loots >= 0:
                self.parking_lots -= 1
                return f"Parking lots available: {self.parking_lots}"
            return f"There are no more parking lots!"
        except TypeError:
            return f"There are no more parking lots!"



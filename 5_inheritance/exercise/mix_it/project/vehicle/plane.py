from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle


class Plane(Vehicle):
    def __init__(self, available_seats, rows, seats_per_row):
        Vehicle.__init__(self, available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

    def buy_tickets(self, row_number, tickets_count):
        if 1 < row_number > self.rows:
            return f"There is no row {row_number} in the plane!"

        if row_number not in self.seats_available.keys():
            self.seats_available[row_number] = self.seats_per_row

        try:
            total_tickets_on_this_row = self.seats_available[row_number] - tickets_count
            if total_tickets_on_this_row >= 0:
                self.seats_available[row_number] -= tickets_count
                return tickets_count
            return f"Not enough tickets on row {row_number}!"
        except TypeError:
            return f"Not enough tickets on row {row_number}!"



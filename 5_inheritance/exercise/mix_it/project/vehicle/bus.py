from project.capacity_mixin import CapacityMixin
from project.vehicle.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, available_seats, ticket_price):
        Vehicle.__init__(self, available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = 0

    def get_ticket(self, tickets_count):
        is_available = CapacityMixin.get_capacity(self.available_seats, tickets_count + self.tickets_sold)
        if isinstance(is_available, int):
            self.tickets_sold += tickets_count


    def get_total_profit(self):
        return self.tickets_sold * self.ticket_price



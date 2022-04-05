from project.capacity_mixin import CapacityMixin
from project.technology.technology import Technology


class Laptop(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_software(self, software, software_memory):
        if software_memory > self.memory - self.memory_taken:
            return f"You don't have enough space for {software}!"
        self.memory_taken += software_memory
        memory_left = self.memory - self.memory_taken
        return memory_left

from project.technology.technology import Technology
from project.capacity_mixin import CapacityMixin


class SmartPhone(Technology):
    def __init__(self, memory, memory_taken):
        Technology.__init__(self, memory, memory_taken)

    def install_apps(self, app, app_memory):
        if app_memory > self.memory - self.memory_taken:
            return f"You don't have enough space for {app}!"
        self.memory_taken += app_memory
        memory_left = self.memory - self.memory_taken
        return memory_left


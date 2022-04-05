from abc import ABC, abstractmethod

from project.food import Meat, Fruit


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        if food == self.DIET:
            print('da')


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        Animal.__init__(self, name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        Animal.__init__(self, name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {float(self.weight)}, {self.living_region}, {self.food_eaten}]"



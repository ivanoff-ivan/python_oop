from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:
    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory,
                 paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        if recipe not in self.storage.keys():
            self.storage[recipe] = 0
        self.storage[recipe] += 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.ingredients.keys() and color in self.paint_factory.ingredients.keys():
            if self.egg_factory.ingredients[egg_type] > 0 and self.paint_factory.ingredients[color] > 0:
                key = f"{color} {egg_type}"
                if key not in self.storage.keys():
                    self.storage[key] = 0
                self.storage[key] += 1
                self.egg_factory.ingredients[egg_type] -= 1
                self.paint_factory.ingredients[color] -= 1
                return
        raise ValueError("Invalid commands")

    def __repr__(self):
        result = f"Shop name: {self.name}\nShop Storage:"
        for k, v in self.storage.items():
            result += f"\n{k}: {v}"
        return result

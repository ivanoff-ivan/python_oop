from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    DIET = ["Vegetable", "Fruit"]
    WEIGHT_INC = 0.1

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in Mouse.DIET:
            return f"Mouse does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Mouse.WEIGHT_INC
        self.food_eaten += food.quantity


class Dog(Mammal):
    DIET = ["Meat"]
    WEIGHT_INC = 0.4

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in Dog.DIET:
            return f"Dog does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Dog.WEIGHT_INC
        self.food_eaten += food.quantity


class Cat(Mammal):
    DIET = ["Meat", "Vegetable"]
    WEIGHT_INC = 0.3

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in Cat.DIET:
            return f"Cat does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Cat.WEIGHT_INC
        self.food_eaten += food.quantity


class Tiger(Mammal):
    DIET = ["Meat"]
    WEIGHT_INC = 1

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in Tiger.DIET:
            return f"Tiger does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Tiger.WEIGHT_INC
        self.food_eaten += food.quantity



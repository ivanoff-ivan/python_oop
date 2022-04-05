from project.animals.animal import Bird


class Owl(Bird):
    DIET = ["Meat"]
    WEIGHT_INC = 0.25

    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in Owl.DIET:
            return f"Owl does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Owl.WEIGHT_INC
        self.food_eaten += food.quantity


class Hen(Bird):
    DIET = ["Vegetable", "Fruit", "Meat", "Seed"]
    WEIGHT_INC = 0.35

    def __init__(self, name, weight, wing_size):
        Bird.__init__(self, name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if food.__class__.__name__ not in Hen.DIET:
            return f"Hen does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * Hen.WEIGHT_INC
        self.food_eaten += food.quantity


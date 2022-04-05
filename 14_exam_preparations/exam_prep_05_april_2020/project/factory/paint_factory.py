from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        possible_ingredients = ["white", "yellow", "blue", "green", "red"]
        if ingredient_type in possible_ingredients:
            if self.can_add(quantity):
                if ingredient_type not in self.ingredients.keys():
                    self.ingredients[ingredient_type] = 0
                self.ingredients[ingredient_type] += quantity
                return
            raise ValueError("Not enough space in factory")
        raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.name}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients.keys():
            if quantity <= self.ingredients[ingredient_type]:
                self.ingredients[ingredient_type] -= quantity
                return
            raise ValueError("Ingredient quantity cannot be less than zero")
        raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients

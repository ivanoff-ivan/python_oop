from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        Factory.__init__(self, name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        possible_ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
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
        raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        self.recipes[recipe_name] = recipe

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes.keys():
            if recipe_name not in self.products.keys():
                self.products[recipe_name] = 0
            self.products[recipe_name] += 1
            for key, value in self.recipes[recipe_name].items():
                self.ingredients[key] -= value
                return
        raise TypeError("No such recipe")

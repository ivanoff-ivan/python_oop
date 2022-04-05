class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: int, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return self.pizza_ordered()

        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
            self.price += ingredient_price * quantity  # ne sum sig dali trqbwa da se umnojava tuk ili shte e cenata za vs
        else:
            self.ingredients[ingredient] = quantity
            self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return self.pizza_ordered()

        if ingredient not in self.ingredients.keys():
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def pizza_ordered(self):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        PizzaDelivery.ordered = True
        ingredients_and_quanties = ", ".join([f"{i}: {q}" for i, q in self.ingredients.items()])
        return f"You've ordered pizza {self.name} prepared with {ingredients_and_quanties} and the price will be {self.price}lv."


import unittest


class Tests(unittest.TestCase):
    def test_remove_ingredient_after_pizza_is_ordered_should_return_message(self):
        t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 1})
        order = t.pizza_ordered()
        result = t.remove_ingredient('mozzarella', 1, 2)
        self.assertEqual(order,
                         "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.")
        self.assertEqual(result, "Pizza Margarita already prepared and we can't make any changes!")


if __name__ == "__main__":
    unittest.main()

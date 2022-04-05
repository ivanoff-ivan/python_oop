import unittest

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(unittest.TestCase):
    def test_initMethod_shouldInitialize(self):
        pf = PaintFactory("test_name", 20)
        self.assertEqual("test_name", pf.name)
        self.assertEqual(20, pf.capacity)
        self.assertEqual({}, pf.ingredients)

    def test_addIngredientMethod_possibleIngredientTypes(self):
        pf = PaintFactory("test_name", 20)
        possible_ingredients = ["white", "yellow", "blue", "green", "red"]
        expected = {}
        for ingr in possible_ingredients:
            pf.add_ingredient(ingr, 1)
            expected[ingr] = 1

        self.assertEqual(expected, pf.ingredients)

    def test_addIngredientMethod_whenEnoughSpaceAndIngrInPossibleIngs_shouldIncQuantityElseRaiseValueError(self):
        pf = PaintFactory("test_name", 20)
        pf.add_ingredient("white", 10)
        self.assertEqual(10, pf.ingredients["white"])
        pf.add_ingredient("white", 10)
        self.assertEqual(20, pf.ingredients["white"])
        with self.assertRaises(ValueError) as context:
            pf.add_ingredient("white", 1)

        self.assertIsNotNone(context.exception)

    def test_addIngredientMethod_whenIngrTypeNotInPossibleIngrs_shouldRaiseTypeError(self):
        pf = PaintFactory("test_name", 20)
        with self.assertRaises(TypeError) as context:
            pf.add_ingredient("purple", 10)

        self.assertIsNotNone(context.exception)

    def test_removeIngredientMethod_whenIngrIngrInIngrs_shouldRemoveItAndDecreaseQuantity_IfQualityBelow0_shouldRaiseValueError(
            self):
        pf = PaintFactory("test_name", 20)
        pf.add_ingredient("white", 10)
        pf.remove_ingredient("white", 5)
        self.assertEqual(5, pf.ingredients["white"])
        pf.remove_ingredient("white", 5)
        self.assertEqual(0, pf.ingredients["white"])
        with self.assertRaises(ValueError) as context:
            pf.remove_ingredient("white", 1)
        self.assertIsNotNone(context.exception)

    def test_removeIngredientMethod_whenIngrNotInIngrs_shouldRaiseKeyError(self):
        pf = PaintFactory("test_name", 20)
        pf.add_ingredient("white", 10)
        with self.assertRaises(KeyError) as context:
            pf.remove_ingredient("blue", 10)

        self.assertIsNotNone(context.exception)

    def test_productsProperty_shouldReturnIngredients(self):
        pf = PaintFactory("test_name", 20)
        pf.add_ingredient("white", 1)
        pf.add_ingredient("blue", 2)
        pf.add_ingredient("yellow", 3)
        expected = {"white": 1, "blue": 2, "yellow": 3}
        self.assertDictEqual(expected, pf.products)

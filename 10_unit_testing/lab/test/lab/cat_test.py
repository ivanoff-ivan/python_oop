import unittest

from lab.cat import Cat


class TestCat(unittest.TestCase):
    def test_catEat_whenCatIsFed_shouldIncreaseItsSize(self):
        """
        Cat's size is increased after eating
        """
        name = "Test name"
        cat = Cat(name)
        cat.eat()
        result = cat.size
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_catEat_whenCatIsFed_fedAttributeShouldBeTrue(self):
        """
        Cat is fed after eating
        """
        name = "Test name"
        cat = Cat(name)
        cat.eat()
        result = cat.fed
        expected_result = True
        self.assertEqual(result, expected_result)

    def test_catEat_whenCatIsAlreadyFed_shouldRaiseAnError(self):
        """
        Cat cannot eat if already fed, raises an error
        """
        name = "Test name"
        cat = Cat(name)
        cat.eat()
        with self.assertRaises(Exception) as context:
            cat.eat()

        self.assertIsNotNone(context.exception)

    def test_catSleep_whenCatIsNotFed_shouldRaiseAnError(self):
        """
        Cat cannot fall asleep if not fed, raises an error
        """
        name = "Test name"
        cat = Cat(name)
        with self.assertRaises(Exception) as context:
            cat.sleep()

        self.assertIsNotNone(context.exception)

    def test_catSleep_afterSleep_catShouldNotBeSleepy(self):
        """
        Cat is not sleepy after sleeping
        """
        name = "Test name"
        cat = Cat(name)
        cat.eat()
        cat.sleep()
        result = cat.sleepy
        expected_result = False
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

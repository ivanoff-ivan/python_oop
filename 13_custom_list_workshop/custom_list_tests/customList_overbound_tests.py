import unittest

from CustomList import CustomList
from errors import CustomException


class CustomListOverboundMethodTests(unittest.TestCase):
    def test_overboundMethod_whenCustomListHasOnlyNumbers_shouldReturnTheIndexOfTheBiggestOne(self):
        cl = CustomList(1, 2, 3, 4.5, 5.5)
        result = cl.overbound()
        expected = 4
        self.assertEqual(expected, result)

    def test_overboundMethod_whenCustomListHasOnlyStrings_shouldReturnTheIndexOfTheBiggestOne(self):
        cl = CustomList("asd", "fg", "qwerty")
        result = cl.overbound()
        expected = 2
        self.assertEqual(expected, result)

    def test_overboundMethod_whenNumbersAndStrings_andTheGreatestValueIsString_shouldReturnTheIndexOfTheString(self):
        cl = CustomList(1, 2, 3.5, 4.5, "asd", "QWERTY")
        result = cl.overbound()
        expected = 5
        self.assertEqual(expected, result)

    def test_overboundMethod_whenNumbersAndStrings_andTheGreatestValueIsNumber_shouldReturnTheIndexOfTheNumber(self):
        cl = CustomList(1, 2, 3.5, 7, "asd", "QWERTY")
        result = cl.overbound()
        expected = 3
        self.assertEqual(expected, result)

    def test_overboundMethod_whenCustomListHasInvalidDataTypes_shouldRaiseCustomException(self):
        cl = CustomList(1, 2, "asd", True)
        with self.assertRaises(CustomException) as context:
            cl.overbound()

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

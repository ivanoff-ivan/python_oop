import unittest

from CustomList import CustomList
from errors import CustomException


class CustomListUnderboundMethodTests(unittest.TestCase):
    def test_underboundMethod_whenCustomListHasOnlyNumbers_shouldReturnTheIndexOfTheSmallestOne(self):
        cl = CustomList(1, 2, 3, 4.5, 5.5)
        result = cl.underbound()
        expected = 0
        self.assertEqual(expected, result)

    def test_underboundMethod_whenCustomListHasOnlyStrings_shouldReturnTheIndexOfTheSmallestOne(self):
        cl = CustomList("asd", "fg", "qwerty")
        result = cl.underbound()
        expected = 1
        self.assertEqual(expected, result)

    def test_underboundMethod_whenNumbersAndStrings_andTheSmallestValueIsString_shouldReturnTheIndexOfTheString(self):
        cl = CustomList(3, 6.5, 4.5, "as", "QWERTY")
        result = cl.underbound()
        expected = 3
        self.assertEqual(expected, result)

    def test_underboundMethod_whenNumbersAndStrings_andTheSmallestValueIsNumber_shouldReturnTheIndexOfTheNumber(self):
        cl = CustomList(1, 2, 3.5, 7, "asd", "QWERTY")
        result = cl.underbound()
        expected = 0
        self.assertEqual(expected, result)

    def test_underboundMethod_whenCustomListHasInvalidDataTypes_shouldRaiseCustomException(self):
        cl = CustomList(1, 2, "asd", True)
        with self.assertRaises(CustomException) as context:
            cl.underbound()

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

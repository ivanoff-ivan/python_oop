import unittest

from CustomList import CustomList
from errors import CustomException


class CustomListSumMethodTests(unittest.TestCase):
    def test_sumMethod_whenCustomListHasOnlyNumbers_shouldReturnTheirSum(self):
        cl = CustomList(1, 2, 3, 4.5, 5.5)
        result = cl.sum()
        expected = 16
        self.assertEqual(expected, result)

    def test_sumMethod_whenCustomListHasOnlyStrings_shouldReturnTheirSum(self):
        cl = CustomList("asd", "fg", "qwerty")
        result = cl.sum()
        expected = 11
        self.assertEqual(expected, result)

    def test_sumMethod_whenCustomListHasNumbersAndStrings_shouldReturnTheirSum(self):
        cl = CustomList(1, 2, 3.5, 4.5, "asd", "QWERTY")
        result = cl.sum()
        expected = 20
        self.assertEqual(expected, result)

    def test_sumMethod_whenCustomListHasInvalidDataTypes_shouldRaiseCustomException(self):
        cl = CustomList(1, 2, "asd", True)
        with self.assertRaises(CustomException) as context:
            cl.sum()

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

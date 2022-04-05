import unittest

from CustomList import CustomList
from errors import CustomIndexError, CustomException


class CustomListMoveMethodTests(unittest.TestCase):

    def test_moveMethod_whenAmountIsLesserThanTheLengthOfTheCustomList_shouldMoveThem(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.move(2)
        expected = [3, 4, 1, 2]
        self.assertEqual(result, expected)

    def test_moveMethod_whenAmountIsEvenToTheLengthOfTheCustomList_shouldReturnTheSameCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.move(4)
        expected = [1, 2, 3, 4]
        self.assertEqual(result, expected)

    def test_moveMethod_whenTheLengthOfTheCustomListIsOneAndTheAmountIsEqualToOne_shouldReturnTheSameCustomList(self):
        cl = CustomList(1)
        result = cl.move(1)
        self.assertEqual([1], result)

    def test_moveMethod_whenTheAmountIsEqualToZero_shouldReturnTheSameCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.move(0)
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, result)

    def test_moveMethod_whenCustomListIsEmpty_shouldReturnEmptyCustomList(self):
        cl = CustomList()
        with self.assertRaises(CustomIndexError) as context:
            cl.move(2)

        self.assertIsNotNone(context.exception)

    def test_moveMethod_whenTheAmountIsNegativeNumber_shouldRaiseCustomException(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomException) as context:
            cl.move(-1)

        self.assertIsNotNone(context.exception)

    def test_moveMethod_whenTheAmountIsGreaterThanTheLengthOfTheCustomList_shouldRaiseCusstomIndexError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomIndexError) as context:
            cl.move(5)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

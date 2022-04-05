import unittest

from CustomList import CustomList
from errors import CustomPopIndexError


class CustomListPopMethodTests(unittest.TestCase):
    def test_popMethod_whenEmptyCustomList_shouldRaiseCustomPopIndexError(self):
        cl = CustomList()
        with self.assertRaises(CustomPopIndexError) as context:
            cl.pop()

        self.assertIsNotNone(context.exception)

    def test_popMethod_whenCustomListIsNotEmpty_shouldPopAndRemoveTheLastElemenet(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.pop()
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()

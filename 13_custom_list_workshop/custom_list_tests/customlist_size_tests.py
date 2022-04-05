import unittest

from CustomList import CustomList


class CustomListSizeMethodTests(unittest.TestCase):
    """
    1.When list is empty
    2.When list is non empty
    """

    def test_sizeMethod_whenCustomListIsEmpty_shouldReturnZero(self):
        cl = CustomList()
        result = cl.size()
        self.assertEqual(0, result)

    def test_sizeMethod_whenCustomListIsNonEmpty_shouldReturnItsLenght(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.size()
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()

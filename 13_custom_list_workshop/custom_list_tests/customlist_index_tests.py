import unittest

from CustomList import CustomList


class CustomListIndexMethodTests(unittest.TestCase):
    def test_indexMethod_whenValueIsInTheList_shouldReturnTheValueIndex(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.index(1)
        self.assertEqual(0, result)

    def test_indexMethod_whenValueOccursMoreThanOnce_shouldReturnTheFirstValueIndex(self):
        cl = CustomList(1, 2, 3, 4, 2)
        result = cl.index(2)
        self.assertEqual(1, result)

    def test_indexMethod_whenValueDoesNotExist_shouldReturnValueNotFound(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.index(5)
        self.assertEqual("Value not found!", result)


if __name__ == '__main__':
    unittest.main()

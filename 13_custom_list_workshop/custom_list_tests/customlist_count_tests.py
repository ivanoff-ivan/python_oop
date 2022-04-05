import unittest

from CustomList import CustomList


class CustomListCountMethodTests(unittest.TestCase):
    def test_countMethod_whenTheValueOccursOneTime_shouldReturnOne(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.count(1)
        self.assertEqual(1, result)

    def test_countMethod_whenTheValueOccursMoreThanOnce_shouldReturnTheOccurance(self):
        cl = CustomList(1, 2, 3, 4, 2, 2)
        result = cl.count(2)
        self.assertEqual(3, result)


if __name__ == '__main__':
    unittest.main()

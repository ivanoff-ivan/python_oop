import unittest

from CustomList import CustomList


class CustomListExtendMethodTests(unittest.TestCase):
    def test_extendMethod_whenCustomListIsEmpty_shouldExtendItAndReturnIt(self):
        elements = [1, 2, 3]
        cl = CustomList()
        result = cl.extend(*elements)
        self.assertListEqual(elements, result)

    def test_extendMethod_whenCustomListHasElements_shouldExtendItAndReturnIt(self):
        elements = [5, 6, 7]
        cl = CustomList(1, 2, 3, 4)
        result = cl.extend(*elements)
        expected = [i for i in range(1, 8)]
        self.assertListEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

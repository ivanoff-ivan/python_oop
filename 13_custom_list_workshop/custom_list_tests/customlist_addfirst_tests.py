import unittest

from CustomList import CustomList


class CustomListAddFirstMethodTests(unittest.TestCase):

    def test_addFirstMethod_whenCustomListIsEmpty_shouldAddTheElement(self):
        cl = CustomList()
        result = cl.add_first(1)
        self.assertEqual([1], result)

    def test_addFirstMethod_whenCustomListIsNonEmpty_shouldAppendLeftTheValue(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.add_first(0)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

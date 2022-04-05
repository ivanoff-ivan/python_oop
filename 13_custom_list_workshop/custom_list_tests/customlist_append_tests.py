import unittest

from CustomList import CustomList


class CustomListAppendMethodTests(unittest.TestCase):
    def test_appendMethod_whenCustomListIsEmpty_shouldAppendAndReturn(self):
        value = 3
        cl = CustomList()
        result = cl.append(value)
        self.assertListEqual([value], result)

    def test_appendMethod_whenCustomListHasElements_shouldAppendAndReturn(self):
        value = 4
        cl = CustomList(1, 2, 3)
        result = cl.append(value)
        self.assertListEqual([1, 2, 3, 4], result)

    def test_appendMethod_whenCustomListHasElementsAndWeAppendMoreThanOneElement_shouldAppendAndReturn(self):
        values = (4, 5)
        cl = CustomList(1, 2, 3)
        result = cl.append(values[0])
        self.assertListEqual([1, 2, 3, 4], result)
        result = cl.append(values[1])
        self.assertListEqual([1, 2, 3, 4, 5], result)


if __name__ == '__main__':
    unittest.main()

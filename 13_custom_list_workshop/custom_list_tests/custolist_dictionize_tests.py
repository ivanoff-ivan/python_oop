import unittest

from CustomList import CustomList


class CustomListDictionizeMethodTests(unittest.TestCase):

    def test_dictionizeMethod_whenCustomListHasEvenElements_shouldDictionizeIt(self):
        cl = CustomList("1", 1, "2", 2)
        result = cl.dictionize()
        expected = {"1": 1, "2": 2}
        self.assertEqual(result, expected)

    def test_dictionizeMethod_whenCustomListHasOddElements_shoudDictionizeItAndPutEmptyStringToTheLastElement(self):
        cl = CustomList("1", 1, "2", 2, "3")
        result = cl.dictionize()
        expected = {"1": 1, "2": 2, "3": " "}
        self.assertEqual(expected, result)

    def test_dictionizeMethod_whenCustomListHasOneElement_shouldDicionizeItAndPutEmptyStringAsValue(self):
        cl = CustomList("1")
        result = cl.dictionize()
        expected = {"1": " "}
        self.assertEqual(expected, result)

    def test_dictionizeMethod_whenCustomListIsEmpty_shouldReturnEmptyCustomDict(self):
        cl = CustomList()
        result = cl.dictionize()
        self.assertEqual({}, result)


if __name__ == '__main__':
    unittest.main()

import unittest

from CustomList import CustomList


class CustomListReverseMethodTests(unittest.TestCase):
    def test_reverseMethod_whenNoElements_shouldReturnEmptyList(self):
        cl = CustomList()
        result = cl.reverse()
        self.assertEqual([], result)

    def test_reverseMethod_whenSingleElement_shouldReturnIt(self):
        cl = CustomList(1)
        result = cl.reverse()
        self.assertEqual([1], result)

    def test_reverseMethod_whenReverseMethodCalled_shouldReturnTheValuesReversed(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.reverse()
        expected = [4, 3, 2, 1]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

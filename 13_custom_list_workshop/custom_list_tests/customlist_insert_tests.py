import unittest

from CustomList import CustomList
from errors import CustomIndexError, CustomTypeError


class CustomListInsertTests(unittest.TestCase):
    def test_insertMethod_whenIndexIsZero_shouldInsertTheElementAndReturnTheCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.insert(0, 10)
        expected = [10, 1, 2, 3, 4]
        self.assertEqual(expected, result)

    def test_insertMethod_whenIndexIsLastElement_shouldInsertTheElementAndReturnTheCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.insert(3, 10)
        expected = [1, 2, 3, 10, 4]
        self.assertEqual(expected, result)

    def test_insertMethod_whenIndexIsFine_shouldInsertTheElementAndReturnTheCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.insert(2, 10)
        expected = [1, 2, 10, 3, 4]
        self.assertEqual(expected, result)

    def test_insertMethod_whenIndexIsMinusOne_shouldInsertTheElementAtTheEndMinusOneAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.insert(-1, 10)
        expected = [1, 2, 3, 10, 4]
        self.assertEqual(expected, result)

    def test_insertMethod_whenIndexIsLenCustomListMinusOne_shouldInsertTheElementAtTheEndMinusOneAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.insert(cl.size() - 1, 10)
        expected = [1, 2, 3, 10, 4]
        self.assertEqual(expected, result)

    def test_insertMethod_whenIndexIsString_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.insert("1", 10)

        self.assertIsNotNone(context.exception)

    def test_insertMethod_whenIndexIsFloat_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.insert(1.2, 10)

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenIndexIsInvalid_shouldRaiseCustomIndexError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomIndexError) as context:
            cl.insert(4, 10)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

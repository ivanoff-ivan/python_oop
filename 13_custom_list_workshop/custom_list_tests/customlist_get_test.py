import unittest

from CustomList import CustomList
from errors import CustomIndexError, CustomTypeError


class CustomListRemoveMethodTests(unittest.TestCase):
    # Happy Cases:
    # 1.

    def test_getMethod_whenIndexIsZero_shouldReturnTheFirstElement(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.get(0)
        self.assertEqual(1, result)

    def test_getMethod_whenIndexIsFine_shouldReturnItsElement(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.get(2)
        self.assertEqual(3, result)

    def test_getMethod_whenIndexIsMinusOne_shouldReturnTheLastElement(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.get(-1)
        self.assertEqual(4, result)

    def test_getMethod_whenIndexIsLenCustomListMinusOne_shouldReturnTheLastElement(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.get(cl.size() - 1)
        self.assertEqual(4, result)

    def test_getMethod_whenIndexIsString_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.get("1")

        self.assertIsNotNone(context.exception)

    def test_getMethod_whenIndexIsFloat_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.get(1.1)

        self.assertIsNotNone(context.exception)

    def test_getMethod_whenIndexIsInvalid_shouldRaiseCustomIndexError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomIndexError) as context:
            cl.get(4)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

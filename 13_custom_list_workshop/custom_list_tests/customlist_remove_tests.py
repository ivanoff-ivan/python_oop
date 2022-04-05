import unittest

from CustomList import CustomList
from errors import CustomIndexError, CustomTypeError


class CustomListRemoveMethodTests(unittest.TestCase):
    def test_removeMethod_whenIndexIsZero_shouldRemoveTheFirstElementAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.remove(0)
        self.assertEqual(1, result)

    def test_removeMethod_whenIndexIsFine_shouldRemoveTheElementAtThisIndexAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.remove(2)
        self.assertEqual(3, result)

    def test_removeMethod_whenIndexIsMinusOne_shouldRemoveTheLastElementAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.remove(-1)
        self.assertEqual(4, result)

    def test_removeMethod_whenIndexIsLenCustomListMinusOne_shouldRemoveTheLastElementAndReturnIt(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.remove(cl.size() - 1)
        self.assertEqual(4, result)

    def test_removeMethod_whenIndexIsString_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.remove("1")

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenIndexIsFloat_shouldRaiseCustomTypeError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomTypeError) as context:
            cl.remove(1.2)

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenIndexIsInvalid_shouldRaiseCustomIndexError(self):
        cl = CustomList(1, 2, 3, 4)
        with self.assertRaises(CustomIndexError) as context:
            cl.remove(4)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

import unittest

from CustomList import CustomList


class CustomListCopyMethodTests(unittest.TestCase):
    def test_copyMethod_whenEmptyCustomList_shouldReturnEmptyCustomList(self):
        cl = CustomList()
        result = cl.copy()
        self.assertEqual([], result)

    def test_copyMethod_whenNonEmptyCustomList_shouldReturnNonEmptyCustomList(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.copy()
        self.assertEqual([1, 2, 3, 4], result)


if __name__ == '__main__':
    unittest.main()

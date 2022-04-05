import unittest

from CustomList import CustomList


class CustomListClearMethodTests(unittest.TestCase):
    def test_clearMethod_whenCustomListHasElementsInIt_shouldClearIt(self):
        cl = CustomList(1, 2, 3, 4)
        cl.clear()
        self.assertListEqual([], cl.items)

    def test_clearMethod_whenCustomListIsEmptyDataAddedAndAfterwardsCleared_shouldBeEmpty(self):
        cl = CustomList()
        result = cl.append(1)
        self.assertEqual([1], result)
        cl.clear()
        self.assertListEqual([], cl.items)


if __name__ == '__main__':
    unittest.main()

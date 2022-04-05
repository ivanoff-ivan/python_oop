import unittest

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
from project.controller import Controller


class PlayerRepositoryTest(unittest.TestCase):
    def test_initMethod_shouldInitialize(self):
        pr = PlayerRepository()
        self.assertEqual(0, pr.count)
        self.assertEqual([], pr.players)

    def test_addMethod_whenPlayerNotInPlayerRepository_shouldAddPlayerAndIncCountByOne(self):
        beg = Beginner("test_name")
        adv = Advanced("advanced_test_name")
        cl = Controller().player_repository
        cl.add(beg)
        self.assertListEqual([beg], cl.players)
        self.assertEqual(1, cl.count)
        cl.add(adv)
        self.assertListEqual([beg, adv], cl.players)
        self.assertEqual(2, cl.count)

    def test_addMethod_whenPlayerWithSuchNameExistsInPlayerRepository_shouldRaiseValueError(self):
        beg = Beginner("test_name")
        adv = Advanced("test_name")
        cl = Controller().player_repository
        cl.add(beg)
        with self.assertRaises(ValueError) as context:
            cl.add(adv)

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenPlayerExistsInPlayerRepository_shouldRemoveHimAndDecreaseCount(self):
        beg = Beginner("test_name")
        adv = Beginner("advanced_test_name")
        cl = Controller().player_repository
        cl.add(beg)
        cl.add(adv)
        self.assertEqual(2, cl.count)
        cl.remove("test_name")
        self.assertEqual([adv], cl.players)
        self.assertEqual(1, cl.count)

    def test_removeMethod_whenEmptyStr_shouldRaiseValueError(self):
        cl = Controller().player_repository
        with self.assertRaises(ValueError) as  context:
            cl.remove("")

        self.assertIsNotNone(context.exception)

    def test_findMethod_whenPlayerNameGiven_shouldReturnThePlayerObject(self):
        beg = Beginner("test_name")
        adv = Advanced("advanced_test_name")
        cl = Controller().player_repository
        cl.add(beg)
        cl.add(adv)
        result = cl.find("test_name")
        self.assertEqual(beg, result)


if __name__ == '__main__':
    unittest.main()

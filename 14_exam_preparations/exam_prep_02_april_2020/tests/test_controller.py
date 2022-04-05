import unittest

from project.card.card_repository import CardRepository
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class ControllerTests(unittest.TestCase):
    def test_initMethod_shouldInitialize(self):
        obj = Controller()
        self.assertIsInstance(obj.player_repository, PlayerRepository)
        self.assertIsInstance(obj.card_repository, CardRepository)

    def test_addPlayerMethod_whenTypeIsBeginner_shouldAddItToPlayerRepository(self):
        obj = Controller()
        result = obj.add_player("Beginner", "test_name")
        expected = "Successfully added player of type Beginner with username: test_name"
        self.assertEqual(result, expected)
        self.assertEqual("test_name", obj.player_repository.players[0].username)
        self.assertEqual(1, obj.player_repository.count)
        self.assertEqual("Beginner", obj.player_repository.players[0].__class__.__name__)

    def test_addPlayerMethod_whenTypeIsAdvanced_shouldAddItToPlayerRepository(self):
        obj = Controller()
        result = obj.add_player("Advanced", "test_name")
        expected = "Successfully added player of type Advanced with username: test_name"
        self.assertEqual(result, expected)
        self.assertEqual("test_name", obj.player_repository.players[0].username)
        self.assertEqual(1, obj.player_repository.count)
        self.assertEqual("Advanced", obj.player_repository.players[0].__class__.__name__)

    def test_addCardMethod_whenTypeIsMagicCard_shouldAddItToCardRepository(self):
        obj = Controller()
        result = obj.add_card("Magic", "test_name")
        expected = "Successfully added card of type MagicCard with name: test_name"
        self.assertEqual(result, expected)
        self.assertEqual("test_name", obj.card_repository.cards[0].name)
        self.assertEqual(1, obj.card_repository.count)
        self.assertEqual("MagicCard", obj.card_repository.cards[0].__class__.__name__)

    def test_addCardMethod_whenTypeIsTrapCard_shouldAddItToCardRepository(self):
        obj = Controller()
        result = obj.add_card("Trap", "test_name")
        expected = "Successfully added card of type TrapCard with name: test_name"
        self.assertEqual(result, expected)
        self.assertEqual("test_name", obj.card_repository.cards[0].name)
        self.assertEqual(1, obj.card_repository.count)
        self.assertEqual("TrapCard", obj.card_repository.cards[0].__class__.__name__)

    def test_addPlayerCardMethod_shouldAddCardToPlayersRepository(self):
        obj = Controller()
        obj.add_player("Beginner", "test_player")
        obj.add_card("Magic", "test_card")
        result = obj.add_player_card("test_player", "test_card")
        expected = "Successfully added card: test_card to user: test_player"
        self.assertEqual(result, expected)
        self.assertEqual("test_card", obj.card_repository.cards[0].name)
        self.assertEqual("test_player", obj.player_repository.players[0].username)

    def test_fightMethod_shouldReturnMessage(self):
        obj = Controller()
        obj.add_player("Beginner", "attacker_test_name")
        obj.add_player("Advanced", "enemy_test_name")
        result = obj.fight("attacker_test_name", "enemy_test_name")
        expected = "Attack user health 90 - Enemy user health 250"
        self.assertEqual(result, expected)

    def test_reportMethod_shouldReturnResult(self):
        obj = Controller()
        obj.add_player("Beginner", "test_name_one")
        obj.add_player("Advanced", "test_name_two")
        obj.add_card("Magic", "test_card_one")
        obj.add_card("Trap", "test_card_two")
        obj.add_player_card("test_name_one", "test_card_one")
        obj.add_player_card("test_name_two", "test_card_two")
        result = obj.report()
        expected = "Username: test_name_one - Health: 50 - Cards 1\n"
        expected += "### Card: test_card_one - Damage: 5\n"
        expected += "Username: test_name_two - Health: 250 - Cards 1\n"
        expected += "### Card: test_card_two - Damage: 120\n"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

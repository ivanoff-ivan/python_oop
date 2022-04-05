import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class CardRepositoryTests(unittest.TestCase):
    def test_initMethod_shouldInitialize(self):
        cr = CardRepository()
        self.assertEqual(0, cr.count)
        self.assertEqual([], cr.cards)

    def test_addMethod_whenCardNotInCards_shouldAddCardAndIncCountByOne(self):
        tc = TrapCard("test_name")
        mc = MagicCard("magic_test_name")
        cr = CardRepository()
        cr.add(tc)
        self.assertEqual([tc], cr.cards)
        self.assertEqual(1, cr.count)
        cr.add(mc)
        self.assertEqual([tc, mc], cr.cards)
        self.assertEqual(2, cr.count)

    def test_addMethod_whenCardNameExistsInCards_shouldRaiseValueError(self):
        tc = TrapCard("test_name")
        mc = MagicCard("test_name")
        cr = CardRepository()
        cr.add(tc)
        with self.assertRaises(ValueError) as context:
            cr.add(mc)

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenEmptyStr_shouldRaiseValueError(self):
        cr = CardRepository()
        with self.assertRaises(ValueError) as context:
            cr.remove("")

        self.assertIsNotNone(context.exception)

    def test_removeMethod_whenCardExists_shouldRemoveItAndDecreaseCount(self):
        tc = TrapCard("test_name")
        mc = MagicCard("magic_test_name")
        cr = CardRepository()
        cr.add(tc)
        cr.add(mc)
        self.assertEqual(2, cr.count)
        cr.remove("test_name")
        self.assertEqual(1, cr.count)
        self.assertEqual([mc], cr.cards)

    def test_findMethod_whenNameIsGiven_shouldReturnCardObject(self):
        tc = TrapCard("test_name")
        mc = MagicCard("magic_test_name")
        cr = CardRepository()
        cr.add(tc)
        cr.add(mc)
        result = cr.find("test_name")
        self.assertEqual(tc, result)


if __name__ == '__main__':
    unittest.main()

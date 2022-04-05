import unittest

from project.card.magic_card import MagicCard


class MagicCardTests(unittest.TestCase):
    def test_initMethod_whenOnlyName_shouldSetDamagePointsTo120AndHealthPointsTo5(self):
        mc = MagicCard("test_name")
        self.assertEqual("test_name", mc.name)
        self.assertEqual(5, mc.damage_points)
        self.assertEqual(80, mc.health_points)

    def test_nameProperty_whenEmptyStr_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            mc = MagicCard("")

        self.assertIsNotNone(context.exception)

    def test_damagePointsProperty_whenBelowZero_shouldRaiseValueError(self):
        mc = MagicCard("test_name")
        with self.assertRaises(ValueError) as context:
            mc.damage_points = -1

        self.assertIsNotNone(context.exception)

    def test_healthPointsProperty_whenBelowZero_shouldRaiseValueError(self):
        mc = MagicCard("test_name")
        with self.assertRaises(ValueError) as context:
            mc.health_points = -1

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

import unittest
from project.card.trap_card import TrapCard


class TrapCardTests(unittest.TestCase):
    def test_initMethod_whenOnlyName_shouldSetDamagePointsTo120AndHealthPointsTo5(self):
        tc = TrapCard("test_name")
        self.assertEqual("test_name", tc.name)
        self.assertEqual(120, tc.damage_points)
        self.assertEqual(5, tc.health_points)

    def test_nameProperty_whenEmptyStr_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            tc = TrapCard("")

        self.assertIsNotNone(context.exception)

    def test_damagePointsProperty_whenBelowZero_shouldRaiseValueError(self):
        tc = TrapCard("test_name")
        with self.assertRaises(ValueError) as context:
            tc.damage_points = -1

        self.assertIsNotNone(context.exception)

    def test_healthPointsProperty_whenBelowZero_shouldRaiseValueError(self):
        tc = TrapCard("test_name")
        with self.assertRaises(ValueError) as context:
            tc.health_points = -1

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()

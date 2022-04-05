import unittest

from project.player.advanced import Advanced


class AdvancedTests(unittest.TestCase):
    def test_initMethod_whenOnlyUsername_shouldSetUpHealthTo250(self):
        adv = Advanced("test_name")
        self.assertEqual("test_name", adv.username)
        self.assertEqual(250, adv.health)

    def test_usernameProperty_whenUsernameIsEmptyStr_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            adv = Advanced("")

        self.assertIsNotNone(context.exception)

    def test_healthProperty_whenHealthIsBelow0_shouldRaiseValueError(self):
        adv = Advanced("test_name")
        with self.assertRaises(ValueError) as context:
            adv.health = -1

        self.assertIsNotNone(context.exception)

    def test_isDeadProperty_whenHealthAboveZero_shouldReturnFalse(self):
        adv = Advanced("test_name")
        self.assertEqual(False, adv.is_dead)

    def test_takeDamageMethod_whenDamagePointsBelowZero_shouldRaiseValueError(self):
        adv = Advanced("test_name")
        with self.assertRaises(ValueError) as context:
            adv.take_damage(-1)

        self.assertIsNotNone(context.exception)

    def test_takeDamageMethod_whenDamagePointsAreAboveZero_shouldDecreaseHealth(self):
        adv = Advanced("test_name")
        adv.take_damage(50)
        self.assertEqual(200, adv.health)


if __name__ == '__main__':
    unittest.main()

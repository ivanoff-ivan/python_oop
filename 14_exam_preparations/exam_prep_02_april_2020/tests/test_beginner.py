import unittest
from project.player.beginner import Beginner


class BeginnerTests(unittest.TestCase):
    def test_initMethod_whenOnlyUsername_shouldSetUpHealthTo50(self):
        beg = Beginner("test_name")
        self.assertEqual("test_name", beg.username)
        self.assertEqual(50, beg.health)

    def test_usernameProperty_whenUsernameIsEmptyStr_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            beg = Beginner("")

        self.assertIsNotNone(context.exception)

    def test_healthProperty_whenHealthIsBelow0_shouldRaiseValueError(self):
        beg = Beginner("test_name")
        with self.assertRaises(ValueError) as context:
            beg.health = -1

        self.assertIsNotNone(context.exception)

    def test_isDeadProperty_whenHealthAboveZero_shouldReturnFalse(self):
        beg = Beginner("test_name")
        self.assertEqual(False, beg.is_dead)

    def test_takeDamageMethod_whenDamagePointsBelowZero_shouldRaiseValueError(self):
        beg = Beginner("test_name")
        with self.assertRaises(ValueError) as context:
            beg.take_damage(-1)

        self.assertIsNotNone(context.exception)

    def test_takeDamageMethod_whenDamagePointsAreAboveZero_shouldDecreaseHealth(self):
        beg = Beginner("test_name")
        beg.take_damage(10)
        self.assertEqual(40, beg.health)


if __name__ == '__main__':
    unittest.main()

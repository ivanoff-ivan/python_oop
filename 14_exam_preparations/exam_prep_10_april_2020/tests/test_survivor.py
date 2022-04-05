import unittest

from project.survivor import Survivor


class SurvivorTests(unittest.TestCase):
    def test_initMethod_whenCorrectNameAndAge_shouldInitialize(self):
        s = Survivor("Georgi", 18)
        self.assertEqual("Georgi", s.name)
        self.assertEqual(18, s.age)
        self.assertEqual(100, s.health)
        self.assertEqual(100, s.needs)

    def test_nameProperty_whenEmptyString_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            Survivor("", 18)

        self.assertIsNotNone(context.exception)

    def test_ageProperty_whenBelowZero_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            Survivor("Georgi", -1)

        self.assertIsNotNone(context.exception)

    def test_healthProperty_whenBelowZero_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            s = Survivor("Georgi", 18)
            s.health = -1

        self.assertIsNotNone(context.exception)

    def test_healthProperty_whenAboveOneHundred_shouldSetItToOneHundred(self):
        s = Survivor("Georgi", 18)
        s.health = 110
        self.assertEqual(100, s.health)

    def test_healthProperty_whenValueIsCorrect_shouldSetIt(self):
        s = Survivor("Georgi", 18)
        s.health = 55
        self.assertEqual(55, s.health)

    def test_needsProperty_whenBelowZero_shouldRaiseValueError(self):
        s = Survivor("Georgi", 18)
        with self.assertRaises(ValueError) as context:
            s.needs = -1

        self.assertIsNotNone(context.exception)

    def test_needsProperty_whenAboveOneHundred_shouldSetItToOneHundred(self):
        s = Survivor("Georgi", 18)
        s.needs = 110
        self.assertEqual(100, s.needs)

    def test_needsProperty_whenCorrectValue_shouldSetIt(self):
        s = Survivor("Georgi", 18)
        s.needs = 55
        self.assertEqual(55, s.needs)

    def test_needsSustenance_whenNeedsAreBlowOneHundred_shouldReturnTrueElseFalse(self):
        s = Survivor("Georgi", 18)
        s.needs = 40
        self.assertEqual(True, s.needs_sustenance)
        s.needs = 100
        self.assertEqual(False, s.needs_sustenance)

    def test_needsHealing_whenHealthIsBlowOneHundred_shouldReturnTrueElseFalse(self):
        s = Survivor("Georgi", 18)
        s.health = 40
        self.assertEqual(True, s.needs_healing)
        s.health = 100
        self.assertEqual(False, s.needs_healing)


if __name__ == '__main__':
    unittest.main()

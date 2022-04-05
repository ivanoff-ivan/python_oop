import unittest
from lab.worker import Worker


class TestWorker(unittest.TestCase):
    def test_workerInit_whenCorrectNameSalaryAndEnergy_shouldBeInitialized(self):
        """
        Test if the worker is initialized with correct name, salary and energy
        """
        name = "Test name"
        salary = 200
        energy = 5
        worker = Worker(name, salary, energy)
        result = [worker.name, worker.salary, worker.energy, worker.money]
        expected_result = [name, salary, energy, 0]
        self.assertListEqual(result, expected_result)

    def test_workerRest_whenRestMethodIsCalled_shouldBeIncremented(self):
        """
        Test if the worker's energy is incremented after the rest method is called
        """
        name = "Test name"
        salary = 200
        energy = 5
        worker = Worker(name, salary, energy)
        worker.rest()
        expected_result = energy + 1
        self.assertEqual(worker.energy, expected_result)

    def test_workerWork_whenEnergyIsBelowZero_exceptionShouldBeRaised(self):
        """
        Test if an error is raised if the worker tries to work with negative energy or equal to 0
        """
        name = "Test name"
        salary = 200
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    def test_workerWork_whenWorkMethodCalled_moneyShouldBeIncreasedByHisSalary(self):
        """
        Test if the worker's money is increased by his salary correctly after the work method is called
        """
        name = "Test name"
        salary = 200
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.money, worker.salary)

    def test_workerWork_whenWorkMethodCalled_energyShouldBeDecreased(self):
        """
        Test if the worker's energy is decreased after the work method is called
        """
        name = "Test name"
        salary = 200
        energy = 5
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.energy, energy - 1)

    def test_workerGetInfo_whenGetInfoMethodCalled_shouldReturnTheProperString(self):
        """
        Test if the get_info method returns the proper string with correct values
        """
        name = "Test name"
        salary = 200
        energy = 5
        worker = Worker(name, salary, energy)
        result = worker.get_info()
        expected_result = "Test name has saved 0 money."
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

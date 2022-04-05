import unittest
from account_balance import Account


class TestAccountBalance(unittest.TestCase):
    def setUp(self):
        self.account_1 = Account("FirstOwner", 50)
        self.account_2 = Account("SecondOwner")

    def test_init_whenCorrectParams_shouldBeInitialized(self):
        self.assertEqual(self.account_1.owner, "FirstOwner")
        self.assertEqual(self.account_1.amount, 50)
        self.assertEqual(self.account_2.owner, "SecondOwner")
        self.assertEqual(self.account_2.amount, 0)

    def test_addTransactionMethod_whenAmountIsNotInt_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            self.account_1.add_transaction(48.54)
        self.assertIsNotNone(context)

    def test_balanceMethod_whenCorrectAmountType_shouldAppendItToTransactionsAndReturnTheSum(self):
        self.account_1.add_transaction(150)
        result = self.account_1.balance
        self.assertEqual(200, result)

    def test_validateTransaction_whenBalanceGetBelowZero_shouldRaiseValueError(self):
        with self.assertRaises(ValueError) as context:
            self.account_1.validate_transaction(self.account_1, -300)
        self.assertIsNotNone(context)

    def test_validateTransaction_whenBalanceIsGreaterThanZero_shouldValidateIt(self):
        result = self.account_1.validate_transaction(self.account_1, 50)
        expected_result = "New balance: 100"
        self.assertEqual(expected_result, result)

    def test_repr_method(self):
        result = repr(self.account_1)
        expected_result = "Account(FirstOwner, 50)"
        self.assertEqual(expected_result, result)

    def test_str_method(self):
        result = str(self.account_1)
        expected_result = "Account of FirstOwner with starting amount: 50"
        self.assertEqual(expected_result, result)

    def test_len_method(self):
        result = len(self.account_1)
        self.assertEqual(0, result)

    def test_getitem_method(self):
        self.account_1.add_transaction(200)
        result = self.account_1[0]
        self.assertEqual(200, result)

    def test_reversed_method(self):
        self.account_1.add_transaction(50)
        self.account_1.add_transaction(100)
        self.account_1.add_transaction(75)
        result = reversed(self.account_1)
        self.assertEqual([75, 100, 50], result)

    def test_equalMethod_whenAccountBalancesAreNotEqual_shouldReturnFalse(self):
        result = self.account_1 == self.account_2
        self.assertEqual(False, result)

    def test_equalMethod_whenBothAccountBalancesAreEqual_shouldReturnTrue(self):
        self.account_2.add_transaction(50)
        result = self.account_1 == self.account_2
        self.assertEqual(True, result)

    def test_lessThanMethod_whenFirstBalanceIsLesserThanSecondBalance_shouldReturnTrue(self):
        result = self.account_2 < self.account_1
        self.assertEqual(True, result)

    def test_lessThanMethod_whenFirstBalanceIsGreaterThanSecondBalance_shouldReturnFalse(self):
        result = self.account_1 < self.account_2
        self.assertEqual(False, result)

    def test_lessThanMethod_whenFirstBalanceIsEqualToTheSecondBalance_shouldReturnFalse(self):
        self.account_2.add_transaction(50)
        result = self.account_1 < self.account_2
        self.assertEqual(False, result)

    def test_lessThanOrEqualMethod_whenBothBalancesAreEqual_shouldReturnTrue(self):
        self.account_2.add_transaction(50)
        result = self.account_1 <= self.account_2
        self.assertEqual(True, result)

    def test_lessThanOrEqualMethod_whenFirstBalanceIsLesserThanTheSecondBalance_shouldReturnTrue(self):
        result = self.account_2 <= self.account_1
        self.assertEqual(True, result)

    def test_lessThanOrEqualMethod_whenFirstBalanceIsGreaterThanTheSecondBalance_shouldReturnFalse(self):
        result = self.account_1 <= self.account_2
        self.assertEqual(False, result)

    def test_greaterThanMethod_whenFirstBalanceIsGreaterThanSecondBalance_shouldReturnTrue(self):
        result = self.account_1 > self.account_2
        self.assertEqual(True, result)

    def test_greaterThanMethod_whenFirstBalanceIsLesserThanSecondBalance_shouldReturnFalse(self):
        result = self.account_2 > self.account_1
        self.assertEqual(False, result)

    def test_greaterThanMethod_whenFirstBalanceIsEqualToTheSecondBalance_shouldReturnFalse(self):
        self.account_2.add_transaction(50)
        result = self.account_1 > self.account_2
        self.assertEqual(False, result)

    def test_greaterThanOrEqualMethod_whenBothBalancesAreEqual_shouldReturnTrue(self):
        self.account_2.add_transaction(50)
        result = self.account_1 >= self.account_2
        self.assertEqual(True, result)

    def test_greaterThanOrEqualMethod_whenFirstBalanceIsGreaterThanTheSecondBalance_shouldReturnTrue(self):
        result = self.account_1 >= self.account_2
        self.assertEqual(True, result)

    def test_greaterThanOrEqualMethod_whenFirstBalanceIsLesserThanTheSecondBalance_shouldReturnFalse(self):
        result = self.account_2 >= self.account_1
        self.assertEqual(False, result)

    def test_add_method(self):
        self.account_1.add_transaction(10)
        self.account_2.add_transaction(5)
        new_account = self.account_1 + self.account_2
        self.assertEqual("FirstOwner&SecondOwner", new_account.owner)
        self.assertEqual(50, new_account.amount)
        self.assertEqual(65, new_account.balance)


if __name__ == '__main__':
    unittest.main()

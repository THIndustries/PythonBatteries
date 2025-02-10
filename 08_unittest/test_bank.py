import unittest
from bank import BankAccount


class BankAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890", 1000)

    def tearDown(self):
        self.account = None

    def test_init(self):
        self.assertEqual(self.account.account_number, "1234567890")
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw_sufficient_balance(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

if __name__ == '__main__':
    unittest.main()
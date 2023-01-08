import unittest

from checking_account import CheckingAccount
from customer import Customer

class TestCheckingAccount(unittest.TestCase):
    NAME = 'ale'
    CPF = '123'
    OCCUPATION = 'dev'

    def setUp(self):
        self.customer = Customer(self.NAME, self.CPF, self.OCCUPATION)
        self.checking_account = CheckingAccount(self.customer, 111, 222)

        self.customer_2 = Customer(self.NAME, self.CPF, self.OCCUPATION)
        self.checking_account_2 = CheckingAccount(self.customer_2, 111, 222)

    def test_verify_if_angency_is_an_integer(self):
        self.assertIsInstance(self.checking_account.agency, int)

    def test_verify_if_agency_number_is_greater_or_equal_than_zero(self):
        self.assertGreaterEqual(self.checking_account.agency, 0)

    def test_verify_if_balance_is_an_integer(self):
        self.assertIsInstance(self.checking_account.balance, int)

    def test_if_the_initial_balance_is_equal_to_zero(self):
        self.assertEqual(self.checking_account.balance, 0)

    def test_if_the_amount_has_been_deposit_in_the_account(self):
        self.checking_account.deposit(10)
        self.assertEqual(self.checking_account.balance, 10)

    def test_if_the_amount_has_been_withdraw_from_the_account(self):
        self.checking_account.deposit(10)
        self.checking_account.withdraw(10)
        self.assertEqual(self.checking_account.balance, 0)

    def test_if_deposit_function_withdraw_the_transfer_value_from_sender_and_sum_to_receiver(self):
        self.checking_account.deposit(10)
        self.checking_account.transfer(10, self.checking_account_2)

        self.assertEqual(self.checking_account.balance, 0)
        self.assertEqual(self.checking_account_2.balance, 10)

if __name__ == '__main__':
    unittest.main()

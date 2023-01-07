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

    def test_verify_if_angency_is_an_integer(self):
        self.assertIsInstance(self.checking_account.agency, int)

    def test_verify_if_agency_number_is_greater_or_equal_than_zero(self):
        self.assertGreaterEqual(self.checking_account.agency, 0)

if __name__ == '__main__':
    unittest.main()

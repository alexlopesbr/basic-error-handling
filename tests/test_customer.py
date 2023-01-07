import unittest

from customer import Customer


class TestCustomer(unittest.TestCase):
    NAME = 'ale'
    CPF = '123'
    OCCUPATION = 'dev'

    def setUp(self):
        self.customer = Customer(self.NAME, self.CPF, self.OCCUPATION)

    def test_create_customer(self):
        self.assertEqual(self.customer.name, self.NAME)
        self.assertEqual(self.customer.cpf, self.CPF)
        self.assertEqual(self.customer.occupation, self.OCCUPATION)

if __name__ == '__main__':
    unittest.main()

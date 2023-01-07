from customer import Customer
from exceptions import InsufficientFundsError, OperationFinantialError


class CheckingAccount:
    total_accounts = 0
    operation_rate = None

    def __init__(self, customer:Customer, agency:int, number:int):
        self.__set_agency(agency)
        self.__balance = 0
        self.customer = customer
        self.__set_number(number)
        self.withdraw_not_alloweds = 0

        CheckingAccount.total_accounts += 1
        CheckingAccount.operation_rate = 30 / CheckingAccount.total_accounts

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, agency:int):
        if not isinstance(agency, int):
            raise ValueError('agency must be an integer', agency)
        if agency <= 0:
            raise ValueError('agency must be bigger than zero')
        self.__agency = agency


    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance:int):
        if not isinstance(balance, int):
            raise ValueError('balance must be an integer')
        self.__balance = balance


    @property
    def number(self):
        return self.__number

    def __set_number(self, number:int):
        if not isinstance(number, int):
            raise ValueError('number must be an integer')
        if number <= 0:
            raise ValueError('number must be bigger than zero')
        self.__number = number

    def transfer(self, value:int, favored):
        if value < 0:
            raise ValueError('value must be greater than or equal to zero')

        try:
            self.withdraw(value)
        except InsufficientFundsError as e:
            e.args = ()
            raise OperationFinantialError(e.message) from e

        favored.deposit(value)

    def withdraw(self, value:int):
        if value < 0:
            raise ValueError('value must be bigger than zero')
        if self.balance < value:
            self.withdraw_not_alloweds += 1
            raise InsufficientFundsError('', self.balance, value)
        self.balance -= value

    def deposit(self, value:int):
        self.balance += value

    def __str__(self) -> str:
        return f'name: {self.customer.name} - balance: {self.balance} - agency: {self.agency}'

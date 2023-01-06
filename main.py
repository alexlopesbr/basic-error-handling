from pprint import pprint

from exceptions import InsufficientFundsError, OperationFinantialError

class Customer:
    def __init__(self, name:str, cpf:str, occupation:str) -> None:
        self.name = name
        self.cpf = cpf
        self.occupation = occupation

    def __str__(self) -> str:
        return f'Name: {self.name}, cpf: {self.cpf}, occupation: {self.occupation}'


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

customer = Customer('Ale', '123.123.123-12', 'dev')
account = CheckingAccount(customer, 123, 123)

customer_2 = Customer('Ale2', '123.123.123-33', 'dev sr')
account_2 = CheckingAccount(customer, 999, 999)


print(account.balance)
account.deposit(300)
print(account.balance)
account.withdraw(100)
print(account.balance)

print(account_2.balance)
account.transfer(500, account_2)
print(account_2.balance)


# account.withdraw(500)





# def main():
#     import sys

#     accounts =[]
#     while(True):
#         try:
#             name = input("Customer name: \n")
#             agency = input("Agency number: \n")
#             number = input("Checking account number: \n")

#             customer = Customer(name, None, None)
#             checkin_account = CheckingAccount(customer, agency, number)
#             accounts.append = checkin_account
#         except ValueError as E:
#             print(type(E.args[1]))
#             sys.exit()
#         except KeyboardInterrupt:
#             print(f"\n\n {len(accounts)} conta(s) criadas")
#             sys.exit()

# if __name__ == "__main__":
#     main()



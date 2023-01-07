from pprint import pprint

from checking_account import CheckingAccount
from customer import Customer
from exceptions import InsufficientFundsError, OperationFinantialError

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
account.transfer(50, account_2)
print(account_2.balance)

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



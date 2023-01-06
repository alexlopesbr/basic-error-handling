class OperationFinantialError(Exception):
    pass


class InsufficientFundsError(OperationFinantialError):
    def __init__(self, message:str='', amount:int=None, value:int=None, *args):
        self.amount = amount
        self.value = value
        msg = f'Insufficient founds. \n Current amount: {self.amount} \n Value: {self.value}'

        super(InsufficientFundsError, self).__init__(message or msg, *args)

class Customer:
    def __init__(self, name:str, cpf:str, occupation:str) -> None:
        self.name = name
        self.cpf = cpf
        self.occupation = occupation

    def __str__(self) -> str:
        return f'Name: {self.name}, cpf: {self.cpf}, occupation: {self.occupation}'

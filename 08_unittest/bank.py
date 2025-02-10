class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number: str = account_number
        self.balance: float = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств")
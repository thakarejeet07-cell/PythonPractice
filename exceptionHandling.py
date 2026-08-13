class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError(f"Cannot withdraw {amount}, balance is only {self.balance}")  
        self.balance -= amount
        print(f"Withdrew {amount}, remaining balance: {self.balance}")


account = BankAccount(5000)

try:
    account.withdraw(6000)
except InsufficientBalanceError as e:
    print(f"Transaction failed: {e}")




class AppError(Exception):
    pass

class PaymentError(AppError):
    pass

class InsufficientFundsError(PaymentError):
    def __init__(self, amount_needed, amount_available):
        self.amount_needed = amount_needed
        self.amount_available = amount_available
        message = f"Need ${amount_needed}, but only ${amount_available} available"
        super().__init__(message)

try:
    raise InsufficientFundsError(500, 200)
except InsufficientFundsError as e:
    print(e)                      
    print(e.amount_needed)       
    print(e.amount_available)       
    shortfall = e.amount_needed - e.amount_available
    print(f"Short by ${shortfall}")





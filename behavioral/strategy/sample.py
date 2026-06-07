from abc import ABC,abstractmethod
from collections import namedtuple

PaymentResult = namedtuple('PaymentResult', ['amount', 'fee'])

class PaymentStrategy(ABC):
    """
    abstract strategy, defines an interface for 
    executing a payment
    """

    @abstractmethod
    def pay(self, amount:float) -> PaymentResult:
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    """
    concrete strategy for credit card payment
    """

    def __init__(self, card_number:str, cvv:str):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount:float) -> PaymentResult:
        fee = amount * 0.02
        print(f"Processing credit card payment of ${amount:.2f} with fee ${fee:.2f} card number {self.card_number}")
        return PaymentResult(amount=amount, fee=fee)

class PayPalPayment(PaymentStrategy):
    """
    concrete strategy for PayPal payment
    """

    def __init__(self, email:str):
        self.email = email

    def pay(self, amount:float) -> PaymentResult:
        fee = amount * 0.01
        print(f"Processing PayPal payment of ${amount:.2f} with fee ${fee:.2f} email {self.email}")
        return PaymentResult(amount=amount, fee=fee)

class CryptoPayment(PaymentStrategy):
    """
    concrete strategy for cryptocurrency payment
    """

    def __init__(self, wallet_address:str):
        self.wallet_address = wallet_address

    def pay(self, amount:float) -> PaymentResult:
        fee = amount * 0.005
        print(f"Processing cryptocurrency payment of ${amount:.2f} with fee ${fee:.2f} wallet address {self.wallet_address}")
        return PaymentResult(amount=amount, fee=fee)

class PaymentContext:
    """
    context class that uses a payment strategy to execute a payment
    - strategy pattern allows us to swap algorithms (payment strategies) 
    at runtime without changing the context class (PaymentContext)
    """

    def __init__(self, payment_strategy:PaymentStrategy):
        self._payment_strategy = payment_strategy
    
    @property
    def payment_strategy(self) -> PaymentStrategy:
        return self._payment_strategy
    
    @payment_strategy.setter
    def payment_strategy(self, strategy:PaymentStrategy):
        if strategy is None:
            raise ValueError("Payment strategy cannot be None")
        self._payment_strategy = strategy

    def execute_payment(self, amount:float) -> PaymentResult:
        return self._payment_strategy.pay(amount)

if __name__ == "__main__":
    context = PaymentContext(CreditCardPayment("1234-5678-9012-3456", "123"))
    context.execute_payment(100.0)

    context.payment_strategy = PayPalPayment("user@example.com")
    context.execute_payment(100.0)

    context.payment_strategy = CryptoPayment("0x1234567890123456789012345678901234567890")
    context.execute_payment(100.0)

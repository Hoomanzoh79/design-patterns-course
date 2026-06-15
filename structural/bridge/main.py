from abc import ABC, abstractmethod

class Payment:
    """
    Abstraction.

    Bridge Pattern:
    - Defines high-level control layer.
    - Holds reference to Implementor.
    - Delegates work instead of implementing it.

    Key Idea:
    Composition over inheritance.
    """

    def __init__(self, gateway: 'PaymentGateway'):
        self.gateway = gateway


class OneTimePayment(Payment):
    """
    Refined Abstraction.

    Bridge Pattern:
    - Extends Abstraction.
    - Adds behavior but delegates core work to Implementor.
    """

    def pay(self, amount: float):
        """
        Bridge in action:

        - Abstraction delegates to Implementor
        - Behavior is composed at runtime
        """
        self.gateway.process_payment(amount)

class SubscriptionPayment(Payment):
    """
    Refined Abstraction.

    Bridge Pattern:
    - Another abstraction variant.
    - Can add extra logic before delegation.
    """

    def pay(self, amount: float):
        self.gateway.process_payment(amount)

class PaymentGateway(ABC):
    """
    Implementor.

    Bridge Pattern:
    - Defines the low-level implementation interface.
    - Does NOT depend on abstraction layer.

    Purpose:
    Decouple implementation from high-level abstraction.
    """

    @abstractmethod
    def process_payment(self, amount: float):
        """Low-level operation implemented by concrete providers."""
        raise NotImplementedError

class StripeGateway(PaymentGateway):
    """
    Concrete Implementor.

    Bridge Pattern:
    - Provides a specific implementation of the Implementor.
    """

    def process_payment(self, amount: float):
        print(f"[Stripe] Processing {amount}")


class PayPalGateway(PaymentGateway):
    """
    Concrete Implementor.

    Bridge Pattern:
    - Another interchangeable implementation of the Implementor.
    """

    def process_payment(self, amount: float):
        print(f"[PayPal] Processing {amount}")

if __name__ == "__main__":
    one_time_payment = OneTimePayment(StripeGateway())
    subscription_payment = SubscriptionPayment(PayPalGateway())

    one_time_payment.pay(100)
    subscription_payment.pay(29.99)

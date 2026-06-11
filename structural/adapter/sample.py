from abc import ABC,abstractmethod

class PaypalPayment:

    def make_payment(self,dollars:str) -> bool:
        print(f"processing paypal payment for {dollars:.2f}$")
        return True
    
    def issue_refund(self,dollars:str) -> bool:
        print(f"processing paypal refund for {dollars:.2f}$")
        return True

class LegacyBankPayment:

    def initiate_transaction(self,currency:str,amount:float,type:str) -> str:
        action = "PAYMENT" if type.lower() in ["pay","payment"] else "REFUND"
        print(f"Processing {action} with legacy bank system for {amount} {currency}")
        return "SUCCESS"

class PaymentAdapter(ABC):

    @abstractmethod
    def pay(self,amount:float,currency:str)->bool:
        raise NotImplementedError
    
    @abstractmethod
    def refund(self,amount:float,currency:str)->bool:
        raise NotImplementedError

class PaypalAdapter(PaymentAdapter):

    def __init__(self,paypal:PaypalPayment):
        self.paypal = paypal
    
    def pay(self,amount:float,currency:str) -> bool:
        if currency.upper() != "USD":
            amount = self._convert_currency(amount,currency,"USD")
        return self.paypal.make_payment(amount)

    def refund(self,amount:float,currency:str) -> bool:
        if currency.upper() != "USD":
            amount = self._convert_currency(amount,currency,"USD")
        return self.paypal.issue_refund(amount)

    def _convert_currency(self,amount:float,from_currency:str,to_currency:str)->float:
        rates = {"EUR":0.85,"USD":1.0}
        return amount * rates[to_currency] / rates[from_currency]

class LegacyBankAdapter(PaymentAdapter):

    def __init__(self,bank:LegacyBankPayment):
        self.bank = bank
    
    def pay(self,amount:float,currency:str) -> bool:
        return self.bank.initiate_transaction(currency,amount,"pay")

    def refund(self,amount:float,currency:str) -> bool:
        return self.bank.initiate_transaction(currency,amount,"refund")

class Ecommerce:

    def __init__(self,payment_method:PaymentAdapter):
        self.payment_method = payment_method
    
    def process_checkout(self,amount:float,currency:str) -> bool:
        print(f"\nProcessing payment for {amount:.2f} {currency}")
        return self.payment_method.pay(amount,currency)

    def process_refund(self,amount:float,currency:str)->bool:
        print(f"\nProcessing refund for {amount:.2f} {currency}")
        return self.payment_method.refund(amount,currency)

if __name__ == '__main__':
    paypal = PaypalPayment()
    bank = LegacyBankPayment()
    paypal_adapter = PaypalAdapter(paypal)
    bank_adapter = LegacyBankAdapter(bank)
    print("------- Using Paypal -------")
    shop = Ecommerce(paypal_adapter)
    shop.process_checkout(amount=13.5,currency="EUR")
    shop.process_refund(amount=20,currency="USD")
    print("------- Using Legacy Bank -------")
    shop = Ecommerce(bank_adapter)
    shop.process_checkout(amount=30,currency="EUR")
    shop.process_refund(amount=26,currency="USD")

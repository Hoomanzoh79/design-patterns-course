from typing import Callable

class Order:
    """
    Context class that uses a discount strategy to calculate the final price of an order
    - strategy pattern allows us to swap algorithms (discount strategies) 
    at runtime without changing the context class (Order)
    """
    def __init__(self, price:float,discount_strategy:Callable[[float], float]):
        self.price = price
        self.discount_strategy = discount_strategy
    
    def get_final_price(self) -> float:
        if self.discount_strategy:
            final_price = self.price - self.discount_strategy(self.price)
            return final_price

        return self.price

def on_sale_discount(price:float) -> float:
    return price * 0.2

def clearance_discount(price:float) -> float:
    return price * 0.5

if __name__ == "__main__":
    order1 = Order(100.0, on_sale_discount)
    print(f"Final price with on sale discount: {order1.get_final_price()}")
    order2 = Order(100.0, clearance_discount)
    print(f"Final price with clearance discount: {order2.get_final_price()}")
    order3 = Order(100.0, None)
    print(f"Final price with no discount: {order3.get_final_price()}")

from abc import ABC,abstractmethod
from datetime import datetime
from typing import Optional

class OrderState(ABC):

    @abstractmethod
    def pay(self):
        raise NotImplementedError
    
    @abstractmethod
    def cancel(self):
        raise NotImplementedError
    
    @abstractmethod
    def ship(self):
        raise NotImplementedError

    @abstractmethod
    def deliver(self):
        raise NotImplementedError
    
    @abstractmethod
    def refund(self,reason:str):
        raise NotImplementedError

class Order:
    def __init__(self,items:list[str],customer_id:int,tracking_number:str,total_price:float):
        self.state : OrderState = PendingOrderState(self)
        self.items = items
        self.customer_id = customer_id
        self.tracking_number = tracking_number
        self.total_price = total_price
        self.created_at:Optional[datetime] = None
        self.paid_at:Optional[datetime] = None
        self.cancelled_at:Optional[datetime] = None
        self.shipped_at:Optional[datetime] = None
        self.delivered_at:Optional[datetime] = None
        self.refund_at:Optional[datetime] = None
    
    def pay(self):
        self.state.pay()
    
    def cancel(self):
        self.state.cancel()
    
    def ship(self):
        self.state.ship()

    def deliver(self):
        self.state.deliver()
    
    def refund(self,reason:str):
        self.state.refund(reason)

class PendingOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("order is paid")
        self.order.state = PaidOrderState(self.order)
        self.order.paid_at = datetime.now()
    
    def cancel(self):
        print("Order is cancelled")
        self.order.state = CancelledOrderState(self.order)
        self.order.cancelled_at = datetime.now()
    
    def ship(self):
        print("Cannot ship an order that's pending")

    def deliver(self):
        print("Cannot deliver an order that's pending")
    
    def refund(self,reason:str):
        print("Cannot refund an order that's not delivered")

class CancelledOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("Cannot pay an order that's cancelled")
    
    def cancel(self):
        print("Order is already cancelled")
    
    def ship(self):
        print("Cannot ship an order that's cancelled")

    def deliver(self):
        print("Cannot deliver an order that's cancelled")
    
    def refund(self,reason:str):
        print("Cannot refund an order that's not delivered")

class PaidOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("order is already paid")
    
    def cancel(self):
        print("Cannot cancel an order that's paid")
    
    def ship(self):
        print("Order is shipped")
        self.order.state = ShippedOrderState(self.order)
        self.order.shipped_at = datetime.now()

    def deliver(self):
        print("Order is delivered")
        self.order.state = DeliveredOrderState(self.order)
        self.order.delivered_at = datetime.now()
    
    def refund(self,reason:str):
        print("Cannot refund an order that's not delivered")

class ShippedOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("order is already paid")
    
    def cancel(self):
        print("Cannot cancel an order that's shipped")
    
    def ship(self):
        print("Order is already shipped")

    def deliver(self):
        print("Order is delivered")
        self.order.state = DeliveredOrderState(self.order)
        self.order.delivered_at = datetime.now()
    
    def refund(self,reason:str):
        print("Cannot refund an order that's not delivered")

class DeliveredOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("order is already paid")
    
    def cancel(self):
        print("Cannot cancel an order that's shipped")
    
    def ship(self):
        print("Order is already shipped")

    def deliver(self):
        print("Order is already delivered")
    
    def refund(self,reason:str):
        print(f"Order is refunded,reason: {reason}")
        self.order.state = RefundOrderState(self.order)
        self.order.refund_at = datetime.now()

class RefundOrderState(OrderState):

    def __init__(self,order:Order):
        self.order = order

    def pay(self):
        print("order is already paid")
    
    def cancel(self):
        print("Cannot cancel an order that's shipped")
    
    def ship(self):
        print("Order is already shipped")

    def deliver(self):
        print("Order is already delivered")
    
    def refund(self,reason:str):
        print(f"Order is already refunded,reason: {reason}")

if __name__ == '__main__':
    order = Order(
        tracking_number="order_0001",
        items=["Jeans","T-shirt"],
        total_price=30.5,
        customer_id=20
    )
    order.pay()
    order.ship()
    order.deliver()
    order.refund(reason="Product was not what I expected")

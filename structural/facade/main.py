"""

INTENT:
    Provide a simplified, unified interface to a set of interfaces in a subsystem.
    The Facade defines a higher-level interface that makes the subsystem easier to use.

WHEN TO USE IT:
    - You want to provide a simple interface to a complex subsystem.
    - There are many interdependent classes or the subsystem keeps growing.
    - You want to layer your subsystems (each layer has a facade as its entry point).
    - You want to decouple clients from subsystem implementation details.

STRUCTURE:
    ┌─────────────┐         ┌──────────────────────────────────────────────┐
    │   Client    │ ──────► │                  Facade                      │
    └─────────────┘         │  - Delegates client calls to subsystems      │
                            │  - Knows nothing about the client            │
                            └──────┬─────────┬──────────┬──────────────────┘
                                   │         │          │
                        ┌──────────┘  ┌──────┘   ┌─────┘
                        ▼             ▼           ▼
                   Subsystem A   Subsystem B  Subsystem C
                   (Inventory)  (Payment)    (Shipping) ...

KEY POINTS:
     The Facade does NOT prevent direct access to subsystems .
     The subsystems have no knowledge of the Facade (no back-references).
     Reduces cognitive load on the caller — one method vs. many moving parts.
     Adding a new subsystem step? Update ONLY the Facade, not every caller.
"""

# subsystems

class InventorySystem:
    def check_availability(self, product_id: int, quantity: int) -> bool:
        print(f"[Inventory]  Checking product={product_id}, qty={quantity}")
        return True


class PaymentSystem:
    def process_payment(self, amount: float) -> bool:
        print(f"[Payment]    Processing ${amount:.2f}")
        return True


class ShippingSystem:
    def schedule_delivery(self, product_id: int, quantity: int, address: str) -> str:
        print(f"[Shipping]   Scheduling product={product_id}, qty={quantity} → {address}")
        return "TRACK_12345"


class NotificationSystem:
    def send_confirmation(self, email: str, order_details: dict):
        print(f"[Notification] Sending confirmation to {email} | details={order_details}")

class OrderFacade:
    """
    Facade for the order-processing subsystem.

    Coordinates InventorySystem, PaymentSystem, ShippingSystem, and
    NotificationSystem behind a single, easy-to-call method so that
    callers never have to orchestrate those subsystems themselves.
    """

    def __init__(
        self,
    ):
        self._inventory = InventorySystem()
        self._payment = PaymentSystem()
        self._shipping = ShippingSystem()
        self._notification = NotificationSystem()

    def place_order(
        self,
        product_id: int,
        quantity: int,
        amount: float,
        address: str,
        email: str,
    ) -> dict:
        print("\n" + "=" * 50)
        print("  ORDER PROCESSING STARTED")
        print("=" * 50)
        if not self._inventory.check_availability(product_id, quantity):
            return self._failure("Insufficient stock for the requested product.")
        if not self._payment.process_payment(amount):
            return self._failure("Payment could not be processed.")
        tracking_id = self._shipping.schedule_delivery(product_id, quantity, address)
        order_details = {
            "product_id": product_id,
            "quantity": quantity,
            "amount": amount,
            "address": address,
            "tracking_id": tracking_id,
        }
        self._notification.send_confirmation(email, order_details)

        print("=" * 50)
        print("  ORDER PROCESSING COMPLETE")
        print("=" * 50 + "\n")

        return {
            "success": True,
            "tracking_id": tracking_id,
            "message": f"Order placed successfully. Track your parcel with {tracking_id}.",
        }

    def cancel_order(self, order_id: str, email: str) -> dict:
        print(f"[Facade] Cancelling order {order_id} for {email} … (stub)")
        return {"success": True, "message": f"Order {order_id} cancelled."}


    @staticmethod
    def _failure(reason: str) -> dict:
        """Centralise failure-response construction so it's consistent."""
        print(f"[Facade] Order failed: {reason}")
        return {"success": False, "tracking_id": None, "message": reason}

if __name__ == "__main__":
    facade = OrderFacade()
    result = facade.place_order(
        product_id=42,
        quantity=3,
        amount=149.99,
        address="123 Main St, Helsinki, FI",
        email="customer@example.com",
    )
    print("Client received:", result)

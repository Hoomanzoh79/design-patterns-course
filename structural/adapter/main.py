from abc import ABC, abstractmethod
"""
Adapter Pattern
===============
Converts the interface of a class into another interface that clients expect.
It lets incompatible interfaces work together without modifying existing code.

Structure:
  Target    – the interface the client expects
  Adaptee   – the existing class with an incompatible interface
  Adapter   – wraps the Adaptee and translates calls to match the Target
  Client    – uses only the Target interface; unaware of the Adaptee
"""


class EuropeanSocket:
    """Adaptee: existing class with an incompatible interface (230V)."""

    def provide_230v(self) -> float:
        """Delivers 230V as used in European outlets."""
        return 230.0


class USASocket(ABC):
    """Target: the interface the client (USADevice) expects (120V)."""

    @abstractmethod
    def provide_120v(self) -> float:
        """Delivers 120V as used in American outlets."""
        raise NotImplementedError


class EuropeanToUSAAdapter(USASocket):
    """
    Adapter: wraps a EuropeanSocket and translates its 230V output
    into the 120V interface that USADevice expects.
    """

    def __init__(self, european_socket: EuropeanSocket) -> None:
        self._european_socket = european_socket

    def provide_120v(self) -> float:
        """Steps 230V down to 120V using a fixed conversion ratio."""
        volts = self._european_socket.provide_230v()
        converted = round(volts / 1.917)   # 230 / 1.917 ≈ 120V
        print(f"Adapter: converting {volts}V -> {converted}V")
        return converted


class USADevice:
    """Client: works exclusively with the USASocket (Target) interface."""

    def __init__(self, socket: USASocket) -> None:
        self._socket = socket

    def turn_on(self) -> None:
        """Powers on using whatever USASocket implementation is injected."""
        volts = self._socket.provide_120v()
        print(f"Device running on {volts}V ")


if __name__ == "__main__":
    # With adapter – plug a European socket into a USA device
    print("--- European socket via adapter ---")
    eu_socket  = EuropeanSocket()
    adapter    = EuropeanToUSAAdapter(eu_socket)
    device     = USADevice(adapter)
    device.turn_on()

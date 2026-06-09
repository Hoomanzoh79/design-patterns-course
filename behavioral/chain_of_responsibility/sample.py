from abc import ABC, abstractmethod
import re
from typing import Optional

class AuthHandler(ABC):
    def __init__(self):
        self._next_handler: Optional['AuthHandler'] = None

    def set_next(self, handler: 'AuthHandler')-> 'AuthHandler':
        self._next_handler = handler
        return handler
    
    def pass_to_next(self, request:dict) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return "Authentication failed: No handler could process the request"
    
    @abstractmethod
    def handle(self, request:dict) -> str:
        raise NotImplementedError

class IPAuthHandler(AuthHandler):
    def handle(self, request:dict) -> str:
        if request.get("ip") in ["192.168.1.1", "192.168.1.2"]:
            print(f"{self.__class__.__name__}: IP address is valid.")
            return self.pass_to_next(request)

        return f"{self.__class__.__name__} : Unauthorized IP address"

class PasswordAuthHandler(AuthHandler):
    def handle(self, request:dict) -> str:
        if request.get("username") == "admin" and request.get("password") == "admin123":
            print(f"{self.__class__.__name__}: Username and password are valid.")
            return self.pass_to_next(request)

        return f"{self.__class__.__name__} : Invalid username or password"

class TwoFactorAuthHandler(AuthHandler):
    def handle(self, request:dict) -> str:
        if request.get("2fa_code") == "123456":
            print(f"{self.__class__.__name__}: 2FA code is valid.")
            return self.pass_to_next(request)

        return f"{self.__class__.__name__} : Invalid 2FA code"

class SessionAuthHandler(AuthHandler):
    def handle(self, request:dict) -> str:
        if request.get("session_token") == "abc123":
            print(f"{self.__class__.__name__}: Session token is valid.")
            return "Authentication successful"

        return f"{self.__class__.__name__} : Invalid session token"

if __name__ == "__main__":
    requests = [
        {
            "ip": "192.168.1.1",
            "username": "admin",
            "password": "admin123",
            "2fa_code": "123456",
            "session_token": "abc123",
        },
        {
            "ip": "192.168.1.2",
            "username": "admin",
            "password": "invalid_password",
            "2fa_code": "123456",
            "session_token": "abc123",
        }
    ]
    auth_chain = IPAuthHandler()
    auth_chain.set_next(PasswordAuthHandler())\
        .set_next(TwoFactorAuthHandler())\
        .set_next(SessionAuthHandler())
    for request in requests:
        print(auth_chain.handle(request))

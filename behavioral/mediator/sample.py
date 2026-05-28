from abc import ABC,abstractmethod
from typing import List

class ChatRoomMediator(ABC):

    @abstractmethod
    def send(self,message:str,sender:"User"):
        raise NotImplementedError
    
    @abstractmethod
    def add_user(self,user:"User"):
        raise NotImplementedError

class ChatRoom(ChatRoomMediator):

    def __init__(self):
        self._users:List["User"] = []

    def send(self,message:str,sender:"User"):
        for user in self._users:
            if user is not sender:
                user.recieve_message(message)
    
    def add_user(self,user:"User"):
        if user not in self._users:
            self._users.append(user)

class User:

    def __init__(self,name:str,mediator:ChatRoomMediator):
        self.name = name
        self._mediator = mediator
        self._mediator.add_user(self)
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return str(self)
    
    def send_message(self,message:str):
        self._mediator.send(message,self)
    
    def recieve_message(self,message:str):
        print(f"User: {self} recieved Message: {message}")

if __name__ == "__main__":
    chatroom = ChatRoom()

    user1 = User("user1",chatroom)
    user2 = User("user2",chatroom)
    user3 = User("user3",chatroom)

    user1.send_message("Hello from user1 !")
    
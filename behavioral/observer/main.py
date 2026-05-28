from abc import ABC,abstractmethod
from typing import Any,List

class Observer(ABC):
    
    @abstractmethod
    def get_notif(self,data:Any):
        raise NotImplementedError

class Subject(ABC):
    def __init__(self):
        self._observers : List[Observer] = []

    def attach(self,observer:Observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self,observer:Observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self,data:Any):
        for observer in self._observers:
            observer.get_notif(data)

class UserOrderSubject(Subject):

    def __init__(self):
        super().__init__()
        self._is_final = False
    
    @property
    def is_final(self):
        return self._is_final

    @is_final.setter
    def is_final(self,value:bool):
        if self._is_final != value:
            self._is_final = value
            self.notify(self)

class SMSNotificationObserver(Observer):

    def get_notif(self, data:Any):
        print(f"SMS notification in {self.__class__.__name__} for {data}")

class EmailNotificationObserver(Observer):

    def get_notif(self, data:Any):
        print(f"Email notification in {self.__class__.__name__} for {data}")

if __name__ == "__main__":
    order = UserOrderSubject()
    order.attach(SMSNotificationObserver())
    order.attach(EmailNotificationObserver())
    order.is_final = True

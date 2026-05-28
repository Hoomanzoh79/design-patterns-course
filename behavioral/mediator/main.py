from abc import ABC,abstractmethod
from typing import List,Any

class Mediator(ABC):

    @abstractmethod
    def notify(self,message:str,sender:Any):
        raise NotImplementedError

class Component:
    def __init__(self,mediator:Mediator,name:str):
        self._mediator = mediator
        self.name = name
    
    def __repr__(self):
        return f"<Component name={self.name} >"
    
    def send(self,message:str):
        self._mediator.notify(message,self)
    
    def recieve(self,message:str):
        print(f"{self} recieved {message}")
    
class ConcreteMediator(Mediator):
    
    def __init__(self):
        self._components:List[Component] = []
    
    def add_component(self,component:Component):
        if component not in self._components:
            self._components.append(component)
    
    def notify(self, message:str, sender:Component):
        for component in self._components:
            if component != sender:
                component.recieve(message)
    
if __name__ == "__main__":
    mediator = ConcreteMediator()

    component1 = Component(mediator=mediator,name="component 1")
    component2 = Component(mediator=mediator,name="component 2")
    component3 = Component(mediator=mediator,name="component 3")

    mediator.add_component(component1)
    mediator.add_component(component2)
    mediator.add_component(component3)

    mediator.notify(message="message from component 1",sender=component1)
    print("--------------------------------------------------------------")
    mediator.notify(message="message from component 3",sender=component3)

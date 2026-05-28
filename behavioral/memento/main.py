from typing import List

# component 1 : memento 
class Memento:
    """
    Manages state 
    the main component to hold state based on the needs of project
    """

    def __init__(self,state:str):
        self._state = state
    
    @property
    def state(self):
        return self._state
    
    def __str__(self):
        return f"<{self._state}>"
    
    def __repr__(self):
        return str(self)

# component 2 : originator 
class Originator:
    """
    Manages memento 
    main component to work with memento
    """

    def __init__(self):
        self._content = ""
    
    def write(self,text:str):
        self._content += text
    
    def save(self) -> Memento:
        """
        creates a memento with its current content
        """
        return Memento(state=self._content)

    def undo(self,memento:Memento):
        """
        gets the previous state from the memento
        """
        if memento:
            self._content = memento.state

# component 3 : caretaker
class CareTaker:
    """
    1. Manages History 
    2. Calls the Originator methods 
    """

    def __init__(self,originator:Originator):
        self._originator = originator
        self._history: List[Memento] = []

    def save_state(self):
        self._history.append(self._originator.save())
    
    def undo_state(self):
        if not self._history:
            return
        self._originator.undo(self._history.pop())
    
    @property
    def history(self):
        return self._history

if __name__ == "__main__":
    originator = Originator()
    caretaker = CareTaker(originator)
    # this is called only to save the first state (which is empty string)
    caretaker.save_state()
    originator.write("Hello")
    caretaker.save_state()
    originator.write(" World")
    caretaker.save_state()
    print(caretaker.history)
    caretaker.undo_state()
    print(caretaker.history)

import copy
from dataclasses import dataclass
from typing import Dict,Any,List

@dataclass
class ConfigMemento:
    settings:Dict[str,Any]
    version:str

class ConfigManager:

    def __init__(self):
        self._settings = {
            "theme":"light",
            "font_size":12,
            "language":"en"
        }
        self._version = "1.0.0"
    
    def change_settings(self,key:str,value:Any):
        if key not in self._settings:
            raise KeyError("this settings doesn't exist")
        self._settings[key] = value

    def create_memento(self) -> ConfigMemento:
        return ConfigMemento(
            settings=copy.deepcopy(self._settings),
            version=self._version
        )
    
    def restore_memento(self,memento:ConfigMemento):
        self._settings = copy.deepcopy(memento.settings)
        self._version = memento.version
    
    def display_settings(self):
        for key,value in self._settings.items():
            print(f"{key} : {value}")
        print("----------------------------------")

    
class ConfigHistory:

    def __init__(self,manager:ConfigManager):
        self._history :List[ConfigMemento] = []
        self._redo_stack : List[ConfigMemento] = []
        self._manager = manager
        self._max_states = 10
    
    def save(self):
        if len(self._history) > self._max_states:
            self._history.pop(0)
        self._history.append(self._manager.create_memento())
        self._redo_stack.clear()

    def undo(self):
        if len(self._history) < 2:  # Need at least 2 states (previous and current)
            raise ValueError("Not enough history to undo")
        
        # Move current state to redo
        current_state = self._history.pop()
        self._redo_stack.append(current_state)
        
        # Restore previous state
        previous_state = self._history[-1]
        self._manager.restore_memento(previous_state)
    
    def redo(self):
        if not self._redo_stack:
            raise ValueError("Redo stack is empty")
        
        next_state = self._redo_stack.pop()
        self._history.append(next_state)
        self._manager.restore_memento(next_state)
    
    @property
    def show_history(self):
        return self._history
    
if __name__ == "__main__":
    config_manager = ConfigManager()
    config_history = ConfigHistory(config_manager)
    config_history.save()
    config_manager.display_settings()
    config_manager.change_settings("language","fa")
    config_history.save()
    config_manager.display_settings()
    config_history.undo()
    config_manager.display_settings()

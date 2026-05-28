from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def handle_click(self)-> str:
        raise NotImplementedError

class TextField(ABC):

    @abstractmethod
    def display(self)-> str:
        raise NotImplementedError

class WindowsButton(Button):

    def handle_click(self)->str:
        return "Windows button clicked !"

class WindowsTextField(TextField):

    def display(self)-> str:
        return "Windows text field displayed !"

class MacButton(Button):

    def handle_click(self)->str:
        return "Mac button clicked !"

class MacTextField(TextField):

    def display(self)-> str:
        return "Mac text field displayed !"

class GUIFactory(ABC):

    @abstractmethod
    def create_button(self)-> Button:
        raise NotImplementedError
    
    @abstractmethod
    def create_textfield(self)-> TextField:
        raise NotImplementedError

class WindowsGUIFactory(GUIFactory):

    def create_button(self)-> Button:
        return WindowsButton()
    
    def create_textfield(self)-> TextField:
        return WindowsTextField()

class MacGUIFactory(GUIFactory):

    def create_button(self)-> Button:
        return MacButton()
    
    def create_textfield(self)-> TextField:
        return MacTextField()

def get_factory_from_user()-> GUIFactory:
    platform = input("please enter your platform: ").lower()
    gui_factories = {
        "windows":WindowsGUIFactory,
        "mac":MacGUIFactory
    }
    if platform in gui_factories:
        return gui_factories[platform]()
    raise ValueError("Invalid platform")

def main():
    factory = get_factory_from_user()
    button = factory.create_button()
    textfield = factory.create_textfield()
    print(button.handle_click())
    print(textfield.display())

if __name__ == "__main__":
    main()

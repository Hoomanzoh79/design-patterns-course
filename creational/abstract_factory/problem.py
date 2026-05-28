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

def main():
    platform = input("please enter your platform: ")
    if platform.lower() == "windows":
        button = WindowsButton()
        text_field = WindowsTextField()
    elif platform.lower() == "mac":
        button = MacButton()
        text_field = MacTextField()
    else:
        raise ValueError("Invalid platform")
    print(button.handle_click())
    print(text_field.display())

if __name__ == "__main__":
    main()

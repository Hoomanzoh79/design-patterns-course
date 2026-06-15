from abc import ABC, abstractmethod
from typing import Optional


class Image(ABC):
    """
    Subject interface.

    Defines the common interface for RealSubject and Proxy.
    """

    @abstractmethod
    def display(self):
        """Display the image."""
        raise NotImplementedError


class RealImage(Image):
    """
    Concrete Subject.

    Represents the real, heavy object.
    Proxy controls access to this object.
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.load()

    def load(self):
        """Simulate expensive initialization (e.g., loading from disk)."""
        print(f"loading image : {self.filename}")

    def display(self):
        """Render the actual image."""
        print(f"displaying image : {self.filename}")


class ImageProxy(Image):
    """
    Proxy.

    Controls access to RealImage.
    Adds lazy initialization (creates object only when needed).
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.real_image: Optional[RealImage] = None

    def display(self):
        """
        Lazily create RealImage and delegate the call.

        Proxy pattern idea:
        - Intercept request
        - Instantiate real object only when required
        - Forward the call
        """
        if self.real_image is None:
            self.real_image = RealImage(self.filename)

        self.real_image.display()


if __name__ == '__main__':
    image = ImageProxy("test_image.png")
    user_input = input("do you want to see the image ? ")
    if user_input.lower() == "yes":
        image.display()
# note : image is only loaded if the user actually wants to see it 
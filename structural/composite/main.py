from abc import ABC, abstractmethod


class Component(ABC):
    """
    Abstract base class for all objects in the composite structure.

    This defines the common interface that both simple objects (leaves)
    and complex objects (composites) must implement.

    Why it exists:
    - It allows client code to treat individual objects and groups
      of objects in the same way.
    """

    @abstractmethod
    def show_details(self):
        raise NotImplementedError

class LeafElement(Component):
    """
    Represents a leaf node in the composite structure.

    A leaf is a basic object that does not contain any children.
    It is the end object in the tree-like structure.

    """

    def __init__(self, position: str):
        self.position = position

    def show_details(self):
        print("\t", end=" ")
        print(self.position)

class CompositeElement(Component):
    """
    Represents a composite node in the structure.

    A composite can contain other components, which may be either:
    - LeafElement objects
    - Other CompositeElement objects

    This makes it possible to build recursive tree structures such as:
    - menus
    - folders
    - organization charts
    - UI components
    """

    def __init__(self, position: str):
        self.position = position
        self.children: list[Component] = []

    def add_element(self, element: Component):
        self.children.append(element)

    def remove_element(self, element: Component):
        self.children.remove(element)

    def show_details(self):
        print(self.position)
        for child in self.children:
            print("\t", end=" ")
            child.show_details()


if __name__ == '__main__':
    """
    Build a simple menu hierarchy and display it.

    Structure:
    main menu
    |- sub menu 1
    |  |- sub menu 1.1
    |  |- sub menu 1.2
    |- sub menu 2
       |- sub menu 2.1
       |- sub menu 2.2
    """
    top_level_menu = CompositeElement("main menu")
    sub_menu1 = CompositeElement("sub menu 1")
    sub_menu2 = CompositeElement("sub menu 2")

    sub_menu11 = LeafElement("sub menu 1.1")
    sub_menu12 = LeafElement("sub menu 1.2")
    sub_menu21 = LeafElement("sub menu 2.1")
    sub_menu22 = LeafElement("sub menu 2.2")

    top_level_menu.add_element(sub_menu1)
    top_level_menu.add_element(sub_menu2)

    sub_menu1.add_element(sub_menu11)
    sub_menu1.add_element(sub_menu12)

    sub_menu2.add_element(sub_menu21)
    sub_menu2.add_element(sub_menu22)

    top_level_menu.show_details()

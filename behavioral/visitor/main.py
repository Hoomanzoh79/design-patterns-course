from abc import ABC, abstractmethod

class Shape(ABC):
    """
    abstract element of the object structure, 
    defines an accept method that takes a visitor 
    """

    @abstractmethod
    def accept(self, visitor:'ShapeVisitor') -> float:
        raise NotImplementedError

class Circle(Shape):
    """
    concrete element of the object structure
    """

    def __init__(self, radius:float):
        self.radius = radius

    def accept(self, visitor:'ShapeVisitor') -> float:
        return visitor.visit_circle(self)

class Rectangle(Shape):
    """
    concrete element of the object structure
    """

    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def accept(self, visitor:'ShapeVisitor') -> float:
        return visitor.visit_rectangle(self)

class ShapeVisitor(ABC):
    """
    abstract visitor, declares a visit method 
    for each concrete element in the object structure
    - Following the Open/Closed Principle, we can add new operations
    without modifying the existing element classes, by creating new visitors
    - we hide the calculation logic in the visitor classes, keeping the element 
    classes simple and focused on their primary responsibilities
    """

    @abstractmethod
    def visit_circle(self, circle:Circle) -> float:
        raise NotImplementedError

    @abstractmethod
    def visit_rectangle(self, rectangle:Rectangle) -> float:
        raise NotImplementedError

class AreaVisitor(ShapeVisitor):
    """
    concrete visitor, implements the visit methods to perform area calculation 
    """

    def visit_circle(self, circle:Circle) -> float:
        return 3.14 * circle.radius * circle.radius

    def visit_rectangle(self, rectangle:Rectangle) -> float:
        return rectangle.width * rectangle.height

class PerimeterVisitor(ShapeVisitor):
    """
    concrete visitor, implements the visit methods to perform perimeter calculation
    """

    def visit_circle(self, circle:Circle) -> float:
        return 2 * 3.14 * circle.radius

    def visit_rectangle(self, rectangle:Rectangle) -> float:
        return 2 * (rectangle.width + rectangle.height)

if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 6)]
    area_visitor = AreaVisitor()
    perimeter_visitor = PerimeterVisitor()

    for shape in shapes:
        print(f"Area for {type(shape).__name__}: {shape.accept(area_visitor)}")
        print(f"Perimeter for {type(shape).__name__}: {shape.accept(perimeter_visitor)}")

# Note : this design pattern might not be used very often

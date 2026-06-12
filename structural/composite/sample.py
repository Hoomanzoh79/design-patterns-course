from abc import ABC,abstractmethod

# region component interface
class Graphic(ABC):

    @abstractmethod
    def render(self):
        raise NotImplementedError
    
    @abstractmethod
    def move(self,x:int,y:int):
        raise NotImplementedError
# endregion

# region leaf elements
class Circle(Graphic):
    def __init__(self,x:int,y:int,radius:int):
        self.x = x
        self.y = y
        self.radius = radius
    
    def render(self):
        print(f"Rendering circle at ({self.x},{self.y}) with radius {self.radius}")
    
    def move(self,x:int,y:int):
        self.x += x
        self.y += y 
        print(f"Moving circle to ({self.x},{self.y})")

class Square(Graphic):
    def __init__(self,x:int,y:int,side:int):
        self.x = x
        self.y = y
        self.side = side
    
    def render(self):
        print(f"Rendering square at ({self.x},{self.y}) with side {self.side}")
    
    def move(self,x:int,y:int):
        self.x += x
        self.y += y 
        print(f"Moving square to ({self.x},{self.y})")
# endregion

# region composite element
class Group(Graphic):
    def __init__(self,name:str):
        self.name = name
        self.graphics : list[Graphic] = []

    def add_graphic(self,element:Graphic):
        self.graphics.append(element)
    
    def remove_graphic(self,element:Graphic):
        self.graphics.remove(element)
    
    def render(self):
        print(f"\nRendering Group : {self.name}")
        for graphic in self.graphics:
            graphic.render()
    
    def move(self,x:int,y:int):
        print(f"\nMoving Group : {self.name}")
        for graphic in self.graphics:
            graphic.move(x,y)
# endregion

if __name__ == '__main__':
    circle_1 = Circle(0,1,3)
    circle_2 = Circle(2,3,4)
    square_1 = Square(5,6,8)
    square_2 = Square(7,9,10)
    group = Group("shapes")
    group.add_graphic(circle_1)
    group.add_graphic(circle_2)
    group.add_graphic(square_1)
    group.add_graphic(square_2)
    group.render()
    group.move(2,2)

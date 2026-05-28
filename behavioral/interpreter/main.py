from abc import ABC,abstractmethod
from typing import Any

# region abstract expression 
class Expression(ABC):

    @abstractmethod
    def interpret(self,value:Any):
        raise NotImplementedError
# endregion

# region terminal expression 
# (expression without any dependency on the others,Ex:numbers like 1,2,3)
class Number(Expression):
    
    def __init__(self,value):
        self.value = value

    def interpret(self,context:Any):
        return self.value
# endregion

# region non-terminal expression 
# (expression with dependency on the others,Ex:operators like +,-,= )
class Add(Expression):

    def __init__(self,left:Number,right:Number):
        self.left = left
        self.right = right

    def interpret(self,context:Any):
        context["number_of_operations"] += 1
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):

    def __init__(self,left:Number,right:Number):
        self.left = left
        self.right = right

    def interpret(self,context:Any):
        context["number_of_operations"] += 1
        return self.left.interpret(context) - self.right.interpret(context)

# endregion

if __name__ == "__main__":
    # (2 + 3) - 1
    expression = Subtract(
        Add(Number(2),Number(3)),
        Number(1)
    )
    # context is not really used in this example
    # so this part isn't crucial,just a mock data
    # context is what every expression recieves
    ctx = {
        "number_of_operations":0
    }
    print(f"Result : {expression.interpret(ctx)}") 
    print(f"Number of math operations: {ctx["number_of_operations"]}")

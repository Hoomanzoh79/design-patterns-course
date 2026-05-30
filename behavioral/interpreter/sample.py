from abc import ABC,abstractmethod
from typing import Any,Callable

class DBContext:
    def __init__(self,data:list[dict]):
        self.data = data

class Expression(ABC):

    @abstractmethod
    def interpret(self,context:DBContext):
        raise NotImplementedError

class Select(Expression):

    def __init__(self,field:str):
        self.field = field
    
    def interpret(self,context:DBContext):
        return [row[self.field] for row in context.data]
    
class Where(Expression):
    
    def __init__(self,condition:Callable[[Any],bool]):
        self.condition = condition
    
    def interpret(self,context:DBContext):
        return [row for row in context.data if self.condition(row)]

class Query(Expression):

    def __init__(self,select:Select,where:Where):
        self.select = select
        self.where = where
    
    def interpret(self,context:DBContext):
        filtered_data = self.where.interpret(context)
        return self.select.interpret(DBContext(filtered_data))

if __name__ == '__main__':
    data = [
        {"name":"Ali","age":23},
        {"name":"Sara","age":19},
        {"name":"Amir","age":17},
        {"name":"Hooman","age":25},
    ]
    context = DBContext(data) 
    result = Query(
        Select("name"),
        Where(lambda row: row["age"] > 20)
    ).interpret(context)
    print(result)

from abc import ABC
from typing import Any
from copy import deepcopy

class Prototype(ABC):

    def before_clone(self,obj:Any,*args, **kwargs):
        return obj
    
    def make_clone(self,obj:Any,*args, **kwargs):
        return deepcopy(obj)
    
    def after_clone(self,obj:Any,*args, **kwargs):
        return obj
    
    def clone(self,*args, **kwargs):
        obj = self.before_clone(self,*args, **kwargs)
        cloned_obj = self.make_clone(obj,*args, **kwargs)
        final_obj = self.after_clone(cloned_obj,*args, **kwargs)
        return final_obj

class MyData(Prototype):

    def __init__(self,name:str,value:str):
        self.name = name
        self.value = value
    
    def before_clone(self, obj, *args, **kwargs):
        """
        For example we want to change the original object 
        as well,before cloning
        - if we override after_clone with this same logic
        only the cloned object will change
        """
        for key,value in kwargs.items():
            if hasattr(obj,key):
                setattr(obj,key,value)
        return obj

if __name__ == '__main__':
    data1 = MyData(name="name1",value="value1")
    data2 = data1.clone(name="name2",value="value2")
    print(data1.name,data1.value)
    print(data2.name,data2.value)

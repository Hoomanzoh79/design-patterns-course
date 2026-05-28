import copy
from uuid import uuid4
from abc import ABC,abstractmethod

class Prototype(ABC):

    @abstractmethod
    def clone(self,*args, **kwargs):
        raise NotImplementedError

class EnemyPrototype(Prototype):
    def __init__(self,name:str,health:int = 0,special_abilities:list = []):
        self.id = uuid4()
        self.name = name
        self.health = health
        self.special_abilities = special_abilities
    
    def clone(self,*args, **kwargs)-> 'EnemyPrototype':
        copy_enemy = copy.deepcopy(self)
        for key,value in kwargs.items():
            setattr(self,key,value)
        return copy_enemy
    
    def __str__(self):
        return f'<ID {self.id} name={self.name} health={self.health} special_abilities={self.special_abilities} />'

zombie1 = EnemyPrototype(name='zombie1',health=100,special_abilities=['self revive'])
zombie2 = zombie1.clone(name='zombie2')
zombie2.special_abilities.append('armor')
print(zombie1)
print(zombie2)
print(zombie1 is zombie2)

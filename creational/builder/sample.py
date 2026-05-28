from abc import ABC,abstractmethod

class Enemy:
    """
    1. Main Product
    """
    def __init__(self):
        self.enemy_type = None
        self.health = 0
        self.weapon = None
        self.abilities = []
    
    def __repr__(self):
        return f'<Enemy type={self.enemy_type} health={self.health} weapon={self.weapon} abilities={self.abilities} />'
    
    def __str__(self):
        return repr(self)

class EnemyBuilder(ABC):
    """
    2.Abstract builder (interface)
    """
    @abstractmethod
    def set_enemy_type(self,enemy_type:str)-> 'EnemyBuilder':
        raise NotImplementedError

    @abstractmethod
    def set_health(self,health:int)-> 'EnemyBuilder':
        raise NotImplementedError
    
    @abstractmethod
    def set_weapon(self,weapon:str)-> 'EnemyBuilder':
        raise NotImplementedError
    
    @abstractmethod
    def add_ability(self,ability:str)-> 'EnemyBuilder':
        raise NotImplementedError
    
    @abstractmethod
    def build(self)-> Enemy:
        raise NotImplementedError

class ConcreteEnemyBuiler(EnemyBuilder):
    """
    3.concrete builder (implementation)
    """
    def __init__(self):
        self.enemy = Enemy()
    
    def set_enemy_type(self,enemy_type:str)-> 'EnemyBuilder':
        self.enemy.enemy_type = enemy_type
        return self

    def set_health(self,health:int)-> 'EnemyBuilder':
        self.enemy.health = health
        return self
    
    def set_weapon(self,weapon:str)-> 'EnemyBuilder':
        self.enemy.weapon = weapon
        return self
    
    def add_ability(self,ability:str)-> 'EnemyBuilder':
        if ability not in self.enemy.abilities:
            self.enemy.abilities.append(ability)
        return self
    
    def build(self)-> Enemy:
        return self.enemy

class EnemyDirector:
    """
    4. Main Director 
    """    
    def __init__(self,builder:EnemyBuilder):
        self.builder = builder
    
    def make_zombie(self)-> Enemy:
        return (self.builder
         .set_enemy_type('zombie')
         .set_health(100)
         .set_weapon('teeth')
         .add_ability('revives itself')
         .build())
    
    def make_warrior(self)-> Enemy:
        return (self.builder
         .set_enemy_type('warrior')
         .set_health(150)
         .set_weapon('sword')
         .add_ability('has a shield')
         .build())

director = EnemyDirector(ConcreteEnemyBuiler())
zombie = director.make_zombie()
print(zombie)
warrior = director.make_warrior()
print(warrior)

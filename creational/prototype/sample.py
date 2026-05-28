import copy
from abc import ABC,abstractmethod
from dataclasses import dataclass
from typing import Dict,List
from itertools import product

class Prototype(ABC):
    @abstractmethod
    def clone(self,*args, **kwargs)->'Prototype':
        raise NotImplementedError

@dataclass
class ProductPrototype(Prototype):
    product_id:str
    name:str
    description:str
    base_price:float
    category:str
    attributes:Dict[str,str]
    images:List[str]
    inventory:int = 0
    sku:str = None
    variation_id:str = None

    def clone(self,*args, **kwargs)->'Prototype':
        clone = copy.deepcopy(self)
        clone.variation_id = f"{self.product_id} - {len(self.attributes) + 1}"
        for attr,val in kwargs.items():
            if attr in clone.attributes:
                clone.attributes[attr] = val
            else:
                clone.attributes[attr] = str(val)
        variation_str = '/'.join([f'{k[:8]} ------> {v[:12]}' for k,v in clone.attributes.items()])
        clone.sku = f'{self.product_id[:8]}-{variation_str}'
        return clone
    
    def __str__(self):
        return f'{self.product_id} ({self.variation_id})- {self.name} - {self.sku} - {self.attributes}'
    
class ProductCatalog:
    def __init__(self):
        self._prototypes : Dict[str,ProductPrototype] = {}

    def add_prototype(self,prototype:'ProductPrototype'):
        self._prototypes[prototype.product_id] = prototype
    
    def create_variation(self,product_id:str,**variation):
        if product_id not in self._prototypes:
            raise ValueError(f"Product with {product_id} not found in the catalog")
        return self._prototypes[product_id].clone(**variation)
    
    def create_variation_set(self, product_id: str, variation_attrs: Dict[str, List]) -> List['Prototype']:
        variations = []
        base_product = self._prototypes[product_id]

        attr_names = list(variation_attrs.keys())
        attr_values = list(variation_attrs.values())

        combs = list(product(*attr_values))
        for combination in combs:
            variation = {attr_names[i]: val for i, val in enumerate(combination)}
            variations.append(base_product.clone(**variation))

        return variations

if __name__ == "__main__":
    catalog = ProductCatalog()
    catalog.add_prototype(ProductPrototype(
        product_id='IPHONE13-001',
        name='iphone 13',
        description='This is iphone 13',
        base_price=1100,
        category='phone',
        attributes={'color':'red','part_number':'zaa'},
        images=["www.s3_bucket.iphone13.png"],
        inventory=200
    ))
    part_number_color_variations = catalog.create_variation_set(
        'IPHONE13-001',
        {
            'color': ['red', 'white', 'black','green'],
            'part_number': ['zaa', 'ch'],
        }
    )

    for i, part_number_color_variation in enumerate(part_number_color_variations):
        print(part_number_color_variation)
        print(f'----- {i + 1} ------')

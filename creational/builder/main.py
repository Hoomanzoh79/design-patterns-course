class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings =  []

    def __repr__(self):
        return f'<Pizza size={self.size} crust={self.crust} toppings={self.toppings} />'
    
    def __str__(self):
        return repr(self)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self,size) -> 'PizzaBuilder':
        if size not in ['thin','thick']:
            raise ValueError("Invalid size")
        self.pizza.size = size
        return self
    
    def set_crust(self,crust) -> 'PizzaBuilder':
        self.pizza.crust = crust
        return self
    
    def add_toppings(self,topping) -> 'PizzaBuilder':
        self.pizza.toppings.append(topping)
        return self
    
    def build(self):
        return self.pizza

if __name__ == '__main__':
    pizza = (
        PizzaBuilder()
        .set_size('thin')
        .set_crust('medium')
        .add_toppings('mushroom')
        .add_toppings('pepperoni')
        .add_toppings('cheese')
        .build()
    )
    print(pizza)

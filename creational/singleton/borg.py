class BorgSingletonClass:
    _shared_state = {}

    def __init__(self):
        self.init_data = "This is init data"

    def __new__(cls,*args, **kwargs):
        obj = super(BorgSingletonClass,cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj

class ChildBordSingleton(BorgSingletonClass):
    pass
    
instance_of_borg_class = BorgSingletonClass()
instance_of_borg_class.my_data = "this is data for main borg class"

instance_of_child_borg_class = ChildBordSingleton()

# False
print(instance_of_borg_class is instance_of_child_borg_class)

print(instance_of_borg_class._shared_state)
print(instance_of_borg_class.__dict__)
print(instance_of_child_borg_class._shared_state)
print(instance_of_child_borg_class.__dict__)

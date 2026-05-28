class SingletonClass:
    _instance = None

    def __init__(self):
        print("__init__ has been called")

    def __new__(cls,*args, **kwargs):
        print("__new__ has been called")
        if cls._instance is None:
            cls._instance = super(SingletonClass,cls).__new__(cls)
        
        return SingletonClass._instance

instance1 = SingletonClass()
instance2 = SingletonClass()
instance3 = SingletonClass()

print(id(instance1))
print(id(instance2))
print(id(instance3))
# True
print(instance1 is instance2)

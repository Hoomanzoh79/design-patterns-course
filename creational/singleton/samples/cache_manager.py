class CacheManager:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super(CacheManager,cls).__new__(cls,*args, **kwargs)
            cls._instance._initialize_cache()
        return cls._instance
    
    def _initialize_cache(self):
        self.cache = {}
    
    def set(self,key,value):
        self.cache[key] = value
    
    def get(self,key):
        return self.cache[key] or None
    
    def clear(self):
        self.cache.clear()

cache_manager1 = CacheManager()
cache_manager2 = CacheManager()
cache_manager1.set("user10","Ali")
cache_manager2.set("user15","Test")

print(cache_manager2.get("user10"))
print(cache_manager1.get("user15"))
print(cache_manager1 is cache_manager2)
cache_manager1.clear()

class ConfigurationManager:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConfigurationManager,cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance
    
    def _load_config(self):
        print("configuration has been loaded,and it's loaded only once")
        self.settings = {
            "db_engine":"postgres",
            "db_host":"localhost",
            "db_port":5432
        }

    def get_setting(self,key):
        return self.settings.get(key,None)
    
config1 = ConfigurationManager()
config2 = ConfigurationManager()
print(config1.get_setting("db_host"))
print(config2.get_setting("db_port"))
# True
print(config1 is config2)

from abc import ABC,abstractmethod

class ConfigurationContext:

    def __init__(self):
        self.settings = {}
    
    def set_value(self,key:str,value:str):
        if value.isdigit():
            self.settings[key] = float(value)
        else:
            self.settings[key] = value
    
    def enable(self,key:str):
        self.settings[key] = True
    
    def disable(self,key:str):
        self.settings[key] = False
    
    def __str__(self):
        return f"{self.settings}"

class Expression(ABC):

    @abstractmethod
    def interpret(self,context:ConfigurationContext):
        raise NotImplementedError

class SetCommand(Expression):

    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def interpret(self,context:ConfigurationContext):
        context.set_value(self.key,self.value)

class EnableCommand(Expression):
    def __init__(self,key):
        self.key = key
    
    def interpret(self,context:ConfigurationContext):
        context.enable(self.key)

class DisableCommand(Expression):
    def __init__(self,key):
        self.key = key
    
    def interpret(self,context:ConfigurationContext):
        context.disable(self.key)

def parse_configs(configs:list[str]) ->list[Expression]:
    expressions = []

    for line in configs:
        tokens = line.split()
        command = tokens[0]
        match command.lower():
            case "enable":
                expressions.append(EnableCommand(tokens[1]))
            case "disable":
                expressions.append(DisableCommand(tokens[1]))
            case "set":
                expressions.append(SetCommand(tokens[1],tokens[2]))
    return expressions

if __name__ == '__main__':
    config_lines = [
        "set timeout 30",
        "set retries 5",
        "enable logging",
        "disable caching",
        "set loglevel info"
    ]
    context = ConfigurationContext()
    expressions = parse_configs(config_lines)
    for expression in expressions:
        expression.interpret(context)
    # This should print -> {
    # 'timeout': 30.0, 
    # 'retries': 5.0, 
    # 'logging': True, 
    # 'caching': False, 
    # 'loglevel': 'info'
    # }
    print(context)

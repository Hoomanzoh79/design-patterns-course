from abc import ABC, abstractmethod
from enum import Enum

class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

class Logger(ABC):
    """
    Abstract base class for loggers in the chain of responsibility.
    """
    def __init__(self, level:LogLevel):
        self.level = level
        self.next_logger = None
    
    def set_next(self, next_logger:'Logger'):
        """
        Sets the next logger in the chain and returns it for chaining
        """
        self.next_logger = next_logger
        return next_logger
    
    def log(self, level:LogLevel, message:str):
        """
        Main method that does the chaining and recursion. 
        If the log level of the message is greater than or equal 
        to the logger's level, it processes the message.
        """
        if self.level.value <= level.value:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log(level, message)
    
    @abstractmethod
    def write(self, message:str):
        raise NotImplementedError

class ConsoleLogger(Logger):
    def write(self, message:str):
        print(f"Console logger: {message}")

class FileLogger(Logger):
    def write(self, message:str):
        print(f"File logger: {message}")

class EmailLogger(Logger):
    def write(self, message:str):
        print(f"Email logger: {message}")

if __name__ == "__main__":
    logger_chain = ConsoleLogger(LogLevel.INFO)
    logger_chain.set_next(FileLogger(LogLevel.WARNING)).set_next(EmailLogger(LogLevel.ERROR))

    logger_chain.log(LogLevel.INFO, "1st log message.")
    logger_chain.log(LogLevel.WARNING, "2nd log message.")
    logger_chain.log(LogLevel.ERROR, "3rd log message.")

# Note : Django is using this pattern for its middleware system. 
# Each middleware can process the request and response, 
# and then pass it to the next middleware in the chain.therefore it's important 
# how you order your middlewares in the settings.py file.
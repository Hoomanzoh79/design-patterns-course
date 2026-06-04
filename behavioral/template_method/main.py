from abc import ABC,abstractmethod
from typing import override

class DataMiner(ABC):
    """
    Main base class that other should inherit 
    and override methods based on their needs
    - this might have a method that forces other classes to implement 
    (if we use abstractmethod)
    - this might not have any abstractmethod at all,still would be fine
    """

    def open(self,path:str)->str:
        return path
    
    def read(self,file:str)->str:
        return f"Reading file: {file}"
    
    def close(self,file:str)->str:
        return f"Closing file : {file}"

    @abstractmethod
    def save_to_db(self,data:str)->str:
        raise NotImplementedError
    
    def manage_data(self,path:str):
        """
        main template method 
        - responsible for calling other methods
        """
        file = self.open(path)
        print(file)
        data = self.read(file)
        print(data)
        result = self.save_to_db(data)
        print(result)
        self.close(file)

class CSVDataMiner(DataMiner):
    """
    Each class can inherit and change those methods based on their needs
    - some might need to change,some might not
    - the methods that are abstractmethod,are forced to be implemented 
    """

    @override
    def open(self,path:str)->str:
        return path
    
    @override
    def read(self,file:str)->str:
        return f"Reading CSV file: {file}"
    
    @override
    def close(self,file:str)->str:
        return f"Closing CSV file : {file}"

    @override
    def save_to_db(self,data:str)->str:
        return f"Saving CSV file {data} to db"

if __name__ == '__main__':
    data_miner = CSVDataMiner()
    data_miner.manage_data(path="my_csv_file.csv")

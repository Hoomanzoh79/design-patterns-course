from abc import ABC,abstractmethod

class Connection(ABC):

    @abstractmethod
    def connect(self):
        raise NotImplementedError
    
    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

class Query(ABC):

    @abstractmethod
    def execute(self,query:str):
        raise NotImplementedError

class DatabaseFactory(ABC):

    @abstractmethod
    def create_connection(self) -> Connection:
        raise NotImplementedError
    
    @abstractmethod
    def create_query(self) -> Query:
        raise NotImplementedError

class PostgresConnection(Connection):

    def connect(self):
        return "Connected to Postgres DB"
    

    def disconnect(self):
         return "Disconnected from Postgres DB"


class MySQLConnection(Connection):

    def connect(self):
        return "Connected to MySQL DB"
    

    def disconnect(self):
         return "Disconnected from MySQL DB"

class PostgresQuery(Query):

    def execute(self,query:str):
        return f"Executing query : {query}"
    
class MySQLQuery(Query):

    def execute(self,query:str):
        return f"Executing query : {query}"

class PostgresDatabaseFactory(DatabaseFactory):

    def create_connection(self)-> Connection:
        return PostgresConnection()
    
    def create_query(self)->Query:
        return PostgresQuery()

class MySQLDatabaseFactory(DatabaseFactory):

    def create_connection(self)-> Connection:
        return MySQLConnection()
    
    def create_query(self)->Query:
        return MySQLQuery()

def get_database_factory() -> DatabaseFactory:
    db = input("select database: ").lower()
    db_factories = {
        "postgres":PostgresDatabaseFactory,
        "mysql":MySQLDatabaseFactory
    }
    if db not in db_factories.keys():
        raise ValueError("DB Not supported yet")
    return db_factories[db]()

if __name__ == "__main__":
    db = get_database_factory()
    connection = db.create_connection()
    print(connection.connect())
    query = db.create_query()
    print(query.execute("SELECT * FROM Users;"))
    print(connection.disconnect())

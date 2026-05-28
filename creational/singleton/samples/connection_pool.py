import sqlite3

class DatabaseConnectionPool:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnectionPool,cls).__new__(cls,*args, **kwargs)
            cls._instance._initialize_pool()

        return cls._instance
    
    def _initialize_pool(self):
        self.connections = []
    
        for _ in range(5):
            conn = sqlite3.connect(":memory:")
            self.connections.append(conn)
    
    def get_connection(self):
        if not self.connections:
            raise Exception("There is no connection in the pool")
        return self.connections.pop()
    
    def release_connection(self,conn):
        self.connections.append(conn)

pool1 = DatabaseConnectionPool()
pool2 = DatabaseConnectionPool()

conn1 = pool1.get_connection()
cursor1 = conn1.cursor()
cursor1.execute("CREATE TABLE products (id INTEGER PRIMARY KEY,name TEXT)")
cursor1.execute("INSERT INTO products (name) VALUES ('iphone')")
conn1.commit()

pool1.release_connection(conn1)
conn2 = pool2.get_connection()
cursor2 = conn2.cursor()
cursor2.execute("SELECT * FROM products")
print(cursor2.fetchall())
pool2.release_connection(conn2)

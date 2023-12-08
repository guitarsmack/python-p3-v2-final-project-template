from models.__init__ import CURSOR, CONN
import datetime

class Client:

    all = {}

    def __init__(self, name, origin, date_joined = None, id = None):
        self.id = id
        self.name = name
        self._date_joined = date_joined
        self.origin = origin
    
    def __repr__(self):
        return f"<Client {self.id}: {self.name}, {self.origin}, {self.date_joined}>"

    @classmethod
    def create_table(cls):
        """Creates a client table, primarily for the seed file"""
        sql = """
        CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        name TEXT,
        origin TEXT,
        date_joined TEXT
        )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls,name,origin):
        client = cls(name,origin)
        client.save()
        return client
    
    def save(self):
        sql = """
        INSERT INTO clients (name,origin,date_joined) VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name,self.origin,self.date_joined))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @property
    def date_joined(self):
        return self._date_joined
    
    @date_joined.setter
    def date_joined(self,date):
        if date is None:
            date = datetime.datetime.now().strftime('%m-%d-%Y')
        self._date_joined = date
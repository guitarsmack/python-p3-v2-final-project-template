from models.__init__ import CONN, CURSOR
from models.client import Client

def seed_database():
    Client.drop_table()
    Client.create_table()

    Client.create('Sonya','Brazil')

seed_database()
print("Sedded")
from models.__init__ import CURSOR, CONN

class Country:

    all = {}

    def __init__(self,name,language):
        self.name = name
        self.language = language
    
    def __repr__(self):
        return f'<Country {self.name}: {self.language}>'
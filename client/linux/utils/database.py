import sqlite3

class DB_Processor:
    def __init__(self, path_ : str):
        self.cursor = None
        self.db = None
        self.path = path_


    def Connect(self):
        self.db = sqlite3.connect(self.path)
        self.cursor = self.db.cursor()
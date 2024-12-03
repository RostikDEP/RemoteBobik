import sqlite3

class DB_Processor:
    def __init__(self, path_ : str):
        self.cursor = None
        self.db = None
        self.path = path_


    def AddInstruction(self, from_: int, to: int, instruction: str, request: str):
        self.Connect()
        sql = f"""INSERT INTO instructions (from_id, to_id, instruction, status, request) VALUES ({from_}, {to}, "{instruction}", "new", "{request}");"""
        self.cursor.execute(sql)
        self.db.commit()
        self.db.close()


    def Connect(self):
        self.db = sqlite3.connect(self.path)
        self.cursor = self.db.cursor()
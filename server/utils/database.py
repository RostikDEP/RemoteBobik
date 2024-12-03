import sqlite3

class DB_Processor:
    def __init__(self, path_ : str):
        self.db = sqlite3.connect(path_)
        self.cursor = self.db.cursor()


    def AddInstruction(self, from_: int, to: int, instruction: str, request: str):
        sql = f"""INSERT INTO instructions (from_id, to_id, instruction, status, request) VALUES ({from_}, {to}, "{instruction}", "new", "{request}");"""
        self.cursor.execute(sql)
        self.db.commit()
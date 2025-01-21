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


    def GetAllInstructions(self):
        self.Connect()
        sql = """SELECT * FROM instructions"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.db.close()
        return result


    def GetInstructionByStatus(self, id_, status):
        self.Connect()
        sql = f"""SELECT * FROM instructions WHERE status like "{status}" AND from_id  like {id_}"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.db.close()
        return result


    def GetInstructionByUncompleted(self, id_):
        self.Connect()
        sql = f"""SELECT * FROM instructions WHERE status not like "done" AND to_id  like {id_}"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.db.close()
        return result


    def WriteImagePathByRecordId(self, id_, filepath):
        self.Connect()
        sql = f"""UPDATE instructions SET request = "{filepath}" WHERE id = {id_}"""
        self.cursor.execute(sql)
        self.db.commit()
        self.db.close()


    def Connect(self):
        self.db = sqlite3.connect(self.path)
        self.cursor = self.db.cursor()

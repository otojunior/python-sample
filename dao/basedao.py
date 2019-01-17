import sqlite3

class BaseDao:
    DB_FILENAME = "/tmp/sample.db"
    
    def __init__(self):
        print("[DEBUG] Base Dao Created, Connection opened")
        self.conn = sqlite3.connect(BaseDao.DB_FILENAME)
    
    def __del__(self):
        print("[DEBUG] Base Dao Destructed, Connection closed")
        self.conn.close()
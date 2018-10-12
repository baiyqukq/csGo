import psycopg2

from common import *

class DB:
    def __init__(self):
        self.database = "ttr"
        self.user = "cr"
        self.passwd = "q"

    def connect(self):
        self.conn = psycopg2.connect(
                database=self.database, 
                user=self.user, 
                password=self.passwd)

        if self.conn == None:
            printt("Can not make connection with DB")
            return False

        self.cursor = self.conn.cursor()
        return True

    def login(self, name, passwd):
        sql = "SELECT * FROM t_account WHERE c_name=%s and c_password=%s"

        self.cursor.execute(sql, (name, passwd))

        rows = self.cursor.fetchall()

        if len(rows) == 1:
            return 0
        else:
            return -1

def _init():
    global g_db
    g_db = None

def setDb(newDb):
    global g_db
    g_db = newDb

def getDb():
    global g_db
    return g_db

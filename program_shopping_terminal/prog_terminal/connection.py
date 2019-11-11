import psycopg2
import atexit

class Connection:

    INSTANCE = None

    def __init__(self):
        __class__.INSTANCE = self
        self.conn = psycopg2.connect(dbname="shopping", user="laurentg", password="", host="localhost")
        atexit.register(self.deconnection)

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, type, value, traceback):
        self.cur.close()
        self.conn.commit()

    def deconnection(self):
        self.conn.close()

    @classmethod
    def get_cursor(cls):
        if cls.INSTANCE == None:
            cls()
        return cls.INSTANCE

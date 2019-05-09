import atexit
import psycopg2
from config import config


class Connection:

    INSTANCE = None

    def __init__(self):
        __class__.INSTANCE = self
        self.params = config()
        try:
            self.conn = psycopg2.connect(**self.params)
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        atexit.register(self.disconnect)

    def __enter__(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.commit()

    def disconnect(self):
        self.conn.close()

    @classmethod
    def get_instance(cls):
        if cls.INSTANCE is None:
            cls()
        return cls.INSTANCE

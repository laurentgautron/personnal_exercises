import psycopg2

class Database():

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="postgres", user="laurentg", password="", host="localhost")
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("DROP DATABASE IF EXISTS Shopping;")
        cur.execute("CREATE DATABASE shopping;")
        cur.close()
        conn.close()

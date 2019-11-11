import psycopg2

class Database():

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="postgres", user="laurentg", password="", host="localhost")
        cur = conn.cursor()
        cur.execute("""SELECT COUNT (*) FROM pg_database WHERE datname = 'shopping';""")
        compteur = cur.fetchone()
        cur.close()
        conn.commit()
        conn.close()
        if compteur == (0,):
            conn = psycopg2.connect(dbname="postgres", user="laurentg", password="", host="localhost")
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute("""CREATE DATABASE shopping;""")
            cur.close()
            conn.close()

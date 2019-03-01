import psycopg2


class Store:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS store (store_id serial PRIMARY KEY, name VARCHAR(100))"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

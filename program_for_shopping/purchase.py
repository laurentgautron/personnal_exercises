import psycopg2


class Purchase:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE purchase (purchase_id serial PRIMARY KEY, date DATE, total_price DECIMAL(4,2), 
                        nb_article INT)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

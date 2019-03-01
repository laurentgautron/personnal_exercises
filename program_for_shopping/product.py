import psycopg2


class Product:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS product (product_id serial PRIMARY KEY, name VARCHAR(100), category VARCHAR(100), 
                        sub_category VARCHAR(100), processed_food BOOLEAN)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

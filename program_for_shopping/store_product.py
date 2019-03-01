import psycopg2


class StoreProduct:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS store_product (product_id INTEGER, store_id INTEGER,
                        PRIMARY KEY(product_id, store_id),
                        CONSTRAINT store_product_product_id_fkey FOREIGN KEY (product_id)
                        REFERENCES product(product_id),
                        CONSTRAINT store_product_store_id_fkey FOREIGN KEY (store_id)
                        REFERENCES store(store_id))"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

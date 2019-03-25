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

    @staticmethod
    def find_product_in_store(store, product):
        conn = psycopg2.connect(dbname="shopping", user="lolo", password="cestmoi", host="localhost")
        cur = conn.cursor()
        cur.execute("""SELECT count(store_id) FROM store_product
                       WHERE product_id = %s AND store_id = %s""", (product, store))
        result = cur.fetchall()
        if not result:
            return False

    def insert(self, store, product):
        if not self.find_product_in_store(store, product):
            conn = psycopg2.connect(dbname="shopping", user="lolo", password="cestmoi", host="localhost")
            cur = conn.cursor()
            cur.execute("INSERT INTO store_product VALUES (%s, %s);", (product, store))
            conn.commit()
            cur.close()
            conn.close()

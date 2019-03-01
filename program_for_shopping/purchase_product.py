import psycopg2


class PurchaseProduct:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase_product (purchase_id INTEGER, product_id INTEGER,
                        PRIMARY KEY (purchase_id, product_id),
                        CONSTRAINT purchase_product_purchase_id_fkey FOREIGN KEY (purchase_id)
                        REFERENCES purchase(purchase_id),
                        CONSTRAINT purchase_product_product_id_fkey FOREIGN KEY (product_id)
                        REFERENCES product(product_id));"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

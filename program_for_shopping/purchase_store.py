import psycopg2


class PurchaseStore:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase_store (purchase_id INTEGER,
                        store_id INTEGER,
                        PRIMARY KEY (purchase_id, store_id),
                        CONSTRAINT purchase_store_purchase_id_fkey FOREIGN KEY(purchase_id)
                        REFERENCES purchase (purchase_id),
                        CONSTRAINT purchase_store_store_id_fkey FOREIGN KEY (store_id)
                        REFERENCES store (store_id));"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self, purchase, store):
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql_insert = """INSERT INTO purchase_store (purchase_id, store_id) VALUES (%s, %s)"""
        cur.execute(sql_insert, (purchase, store))
        conn.commit()
        cur.close()
        conn.close()

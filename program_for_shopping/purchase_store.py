from connection import Connection


class PurchaseStore:

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            sql_create = """CREATE TABLE IF NOT EXISTS purchase_store (purchase_id INTEGER,
                            store_id INTEGER,
                            PRIMARY KEY (purchase_id, store_id),
                            CONSTRAINT purchase_store_purchase_id_fkey FOREIGN KEY(purchase_id)
                            REFERENCES purchase (purchase_id),
                            CONSTRAINT purchase_store_store_id_fkey FOREIGN KEY (store_id)
                            REFERENCES store (store_id));"""
            cur.execute(sql_create)

    @staticmethod
    def insert(purchase, store):
        with Connection.get_instance() as cur:
            sql_insert = """INSERT INTO purchase_store (purchase_id, store_id) VALUES (%s, %s)"""
            cur.execute(sql_insert, (purchase, store))

from connection import Connection


class StoreProduct:

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            sql_create = """CREATE TABLE IF NOT EXISTS store_product (product_id INTEGER, store_id INTEGER,
                            PRIMARY KEY(product_id, store_id),
                            CONSTRAINT store_product_product_id_fkey FOREIGN KEY (product_id)
                            REFERENCES product(product_id),
                            CONSTRAINT store_product_store_id_fkey FOREIGN KEY (store_id)
                            REFERENCES store(store_id))"""
            cur.execute(sql_create)

    @staticmethod
    def find_product_in_store(store, product):
        with Connection.get_instance() as cur:
            cur.execute("""SELECT count(store_id) FROM store_product
                           WHERE product_id = %s AND store_id = %s""", (product, store))
            result = cur.fetchone()
        if result[0] == 0:
            return False
        else:
            return True

    def insert(self, store, product):
        print(self.find_product_in_store(store, product))
        if not self.find_product_in_store(store, product):
            with Connection.get_instance() as cur:
                cur.execute("INSERT INTO store_product VALUES (%s, %s);", (product, store))

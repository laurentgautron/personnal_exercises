from connection import Connection


class PurchaseProduct:

    @staticmethod
    def insert_menu():
        price = float(input('entrer le prix du produit: ').replace(',', '.'))
        weight = float(input('entrer le poids du produit (taper entrée si null): ').replace(',', '.'))
        return price, weight

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            sql_create = """CREATE TABLE IF NOT EXISTS purchase_product (
                            id SERIAL PRIMARY KEY,
                            purchase_id INTEGER, 
                            product_id INTEGER,
                            price DECIMAL(5,2),
                            weight DECIMAL(6,3));"""
            cur.execute(sql_create)

    def insert(self, last_purchase, product):
        with Connection.get_instance() as cur:
            sql_insert = """INSERT INTO purchase_product(purchase_id, product_id, price, weight) VALUES (%s, %s, %s, %s);"""
            price, weight = self.insert_menu()
            cur.execute(sql_insert, (last_purchase, product, price, weight))

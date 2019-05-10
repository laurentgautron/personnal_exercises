from connection import Connection
from ask import Ask

class PurchaseProduct:

    @staticmethod
    def insert_menu():
        price = Ask.ask_number('entrer le prix du produit: ', price=True)
        return price

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            sql_create = """CREATE TABLE IF NOT EXISTS purchase_product (
                            id SERIAL PRIMARY KEY,
                            purchase_id INTEGER, 
                            product_id INTEGER,
                            price DECIMAL(5,2));"""
            cur.execute(sql_create)

    def insert(self, last_purchase, product):
        with Connection.get_instance() as cur:
            sql_insert = """INSERT INTO purchase_product(purchase_id, product_id, price) 
                            VALUES (%s, %s, %s);"""
            price = self.insert_menu()
            cur.execute(sql_insert, (last_purchase, product, price))

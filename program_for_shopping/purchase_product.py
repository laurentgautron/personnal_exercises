import psycopg2


class PurchaseProduct:

    @staticmethod
    def insert_menu():
        #search product in store_product if product is already recovered
        price = input('entrer le prix du produit: ')
        weight = input('entrer le poids du produit (taper entrée si null): ')
        return price, weight

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase_product (
                        purchase_id INTEGER, 
                        product_id INTEGER,
                        price DECIMAL(5,2),
                        weight DECIMAL(6,3),
                        PRIMARY KEY (purchase_id, product_id),
                        CONSTRAINT purchase_product_purchase_id_fkey FOREIGN KEY (purchase_id)
                        REFERENCES purchase(purchase_id),
                        CONSTRAINT purchase_product_product_id_fkey FOREIGN KEY (product_id)
                        REFERENCES product(product_id));"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self, last_purchase, product):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO purchase_product(purchase_id, product_id, price, weight) VALUES (%s, %s, %s, %s);"""
        cur.execute(sql_insert, (last_purchase, product, self.insert_menu()))
        conn.commit()
        cur.close()
        conn.close()

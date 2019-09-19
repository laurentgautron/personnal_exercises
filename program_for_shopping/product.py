import json
from store_product import StoreProduct
from purchase_product import PurchaseProduct
from new import New
from connection import Connection
from ask import Ask


class Product:

    def __init__(self):
        self.store_product = StoreProduct()
        self.purchase_product = PurchaseProduct()

    @staticmethod
    def find_last_product():
        with Connection.get_instance() as cur:
            sql = """ SELECT product_name FROM product
                      JOIN purchase_product ON product.product_id = purchase_product.product_id
                      WHERE purchase_product.id = (SELECT MAX(purchase_product.id) 
                      FROM purchase_product);"""
            cur.execute(sql)
            last_product = cur.fetchone()
        print('le last est', last_product[0])
        return last_product[0]

    @staticmethod
    def insert(result):
        with Connection.get_instance() as cur:
            sql_insert = """INSERT INTO product(product_name, product_category, sub_category, 
                            food, processed_food, weight) VALUES(%s, %s, %s, %s, %s, %s);"""
            cur.execute(sql_insert, result)
        with Connection.get_instance() as cur:
            cur.execute("SELECT product_id FROM product WHERE product_id = (SELECT max(product_id) FROM product);")
            product_id = cur.fetchone()
        return product_id[0]

    def insert_product(self, product_name):
        with Connection.get_instance() as cur:
            cur.execute("SELECT product_id FROM product WHERE product.product_name = %s;", (product_name,))
            result = cur.fetchone()
        if not result:
            weight = Ask.ask_number('entrer le poids du produit: ', weight=True)
            data_list = New.new_product()
            result = product_name, data_list[0], data_list[1], data_list[2], data_list[3], weight
            print(result)
            product_id = self.insert(result)
        else:
            product_id = result[0]
        return product_id

    def record_product(self, last_purchase, nb_articles, store, day, hour, last_article):
        for article in range(last_article, nb_articles):
            print('enregistrer l\'article n° ', article + 1)
            product_name = input('entrez le nom du produit: (taper exit à la place du nom pour quitter en cours) ')
            if product_name != 'exit':
                product = self.insert_product(product_name)
                print('les produtis et stores', product, store)
                self.store_product.insert(store, product)
                self.purchase_product.insert(last_purchase, product)
            else:
                print("à plus tard")
                print('le dernier article avant quitter', article)
                if article == 0:
                    product_name = 'pas de produit enregistré'
                else:
                    product_name = Product.find_last_product()
                list_record = {"purchase": last_purchase, "product": product_name, "store": store,
                               "article": article, "nb_articles": nb_articles, "day": day, "hour": hour}
                with open('list_record.json', 'w') as file:
                    json.dump(list_record, file, indent=4)
                break

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            sql_create = """CREATE TABLE IF NOT EXISTS product (
                            product_id serial PRIMARY KEY,
                            product_name VARCHAR(100),
                            product_category VARCHAR(100),
                            sub_category VARCHAR(100),
                            food BOOLEAN,
                            processed_food BOOLEAN,
                            weight DECIMAL(6,3));"""
            cur.execute(sql_create)

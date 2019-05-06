import psycopg2
import json
from store_product import StoreProduct
from purchase_product import PurchaseProduct
from new import New


class Product:

    def __init__(self):
        self.store_product = StoreProduct()
        self.purchase_product = PurchaseProduct()

    @staticmethod
    def find_last_product():
        conn = psycopg2.connect(dbname="shopping", user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql = """ SELECT product_name FROM product
                  JOIN purchase_product ON purchase_product.id = (SELECT MAX(purchase_product.id) 
                  FROM purchase_product)"""
        cur.execute(sql)
        last_product = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return last_product[0]

    @staticmethod
    def insert(result):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO product(product_name, product_category, sub_category, food, processed_food)
                        VALUES(%s, %s, %s, %s, %s);"""
        cur.execute(sql_insert, result)
        conn.commit()
        cur.close()
        conn.close()
        conn = psycopg2.connect(dbname="shopping", user="lolo", password="cestmoi", host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE product_id = (SELECT max(product_id) FROM product);")
        product_id = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return product_id[0]

    def insert_product(self, product_name):
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE product.product_name = %s;", (product_name,))
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if not result:
            data_list = New.new_product()
            result = product_name, data_list[0], data_list[1], data_list[2], data_list[3]
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
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS product (
                        product_id serial PRIMARY KEY,
                        product_name VARCHAR(100),
                        product_category VARCHAR(100),
                        sub_category VARCHAR(100),
                        food BOOLEAN,
                        processed_food BOOLEAN)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

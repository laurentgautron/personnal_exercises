import os
import json
import psycopg2
from purchase import Purchase
from store import Store
from product import Product
from purchase_store import PurchaseStore
from purchase_product import PurchaseProduct
from store_product import StoreProduct


class Shopping:

    def __init__(self):
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql_init = """ALTER DATABASE shopping SET datestyle TO 'ISO, DMY';"""
        cur.execute(sql_init)
        conn.commit()
        cur.close()
        conn.close()
        self.purchase = Purchase()
        self.store = Store()
        self.product = Product()
        self.purchase_product = PurchaseProduct()
        self.purchase_store = PurchaseStore()
        self.store_product = StoreProduct()

    @staticmethod
    def create_tables():
        Purchase.create()
        Store.create()
        Product.create()
        PurchaseStore.create()
        PurchaseProduct.create()
        StoreProduct.create()

    def insert_datas(self):
        purch = 'o'
        while purch == 'o':
            last_article = 0
            if os.path.isfile('list_record.json'):
                # last_purchase, store, article, nb_article = display_last_datas()
                # remove list_record.json
                with open('list_record.json', 'r') as file:
                    list_record = json.load(file)
                last_purchase = list_record["purchase"]
                product_name = list_record["product"]
                last_article = list_record["article"]
                store = list_record["store"]
                nb_articles = list_record["nb_articles"]
                day = list_record["day"]
                hour = list_record["hour"]
                print("vous avez un enregistrement d'achat en cours!")
                print("le dernier produit enregistré est:", list_record["last_product"])
                print("du magasin:", list_record["store"])
                print("le %s à %s heure", (list_record['day'], list_record["hour"]))
            else:
                last_purchase, nb_articles, day, hour = self.purchase.insert()
                store = self.store.insert_store()
                self.purchase_store.insert(last_purchase, store)
            for article in range(last_article, nb_articles):
                print('enregistrer l\'article n° ', article + 1)
                product_name = input('entrez le nom du produit: (taper e à la place du nom pour quitter en cours)')
                if product_name != 'e'
                    product = self.product.insert_product(product_name)
                    self.store_product.insert(store, product)
                    self.purchase_product.insert(last_purchase, product)
                else:
                    # list_record = self.last_record(last_purchase, product_name, store, article, nb_articles, day, hour)
                    print("à plus tard")
                    list_record = {"purchase": last_purchase, "product": product_name, "store": store, "article": article, "nb_articles": nb_articles, "day": day, "hour": hour}
                    with open('list_record.json', 'w') as file:
                        json.dump(list_record, file, indent=4)
                    break
            purch = input('enregistrer un autre achat (o/n)? ')


if __name__ == "__main__":
    shopping = Shopping()
    shopping.create_tables()
    shopping.insert_datas()

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
            last_purchase, nb_articles = self.purchase.insert()
            store = self.store.insert_store()
            self.purchase_store.insert(last_purchase, store)
            for article in range(0, nb_articles):
                print('enregistrer l\'article n° ', article + 1)
                product = self.product.insert_product()
                self.store_product.insert(store, product)
                self.purchase_product.insert(last_purchase, product)
            purch = input('enregistrer un autre achat (o/n)? ')


if __name__ == "__main__":
    shopping = Shopping()
    shopping.create_tables()
    shopping.insert_datas()

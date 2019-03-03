import psycopg2
from purchase import Purchase
from store import Store
from product import Product
from purchase_store import PurchaseStore
from purchase_product import PurchaseProduct
from store_product import StoreProduct


class DatabaseConnection:

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

    @staticmethod
    def create_tables():
        Purchase.create()
        Store.create()
        Product.create()
        PurchaseStore.create()
        PurchaseProduct.create()
        StoreProduct.create()

    def insert_datas(self):
        self.purchase.insert()
        self.store.insert()
        self.product.insert()
        self.purchase_product.insert()
        #PurchaseProduct.insert()
        #StoreProduct.insert()

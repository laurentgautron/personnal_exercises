import psycopg2
from purchase import Purchase
from store import Store
from product import Product
from purchase_store import PurchaseStore
from purchase_product import PurchaseProduct
from store_product import StoreProduct


class DatabaseConnection:

    @staticmethod
    def create_tables():
        Purchase.create()
        Store.create()
        Product.create()
        PurchaseStore.create()
        PurchaseProduct.create()
        StoreProduct.create()

    @staticmethod
    def insert_datas():
        Purchase.insert()
        #Store.insert()
        #Product.insert()
        #PurchaseStore.insert()
        #PurchaseProduct.insert()
        #StoreProduct.insert()

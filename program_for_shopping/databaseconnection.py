from purchase import Purchase
from store import Store
from product import Product
from purchase_store import PurchaseStore
from purchase_product import PurchaseProduct
from store_product import StoreProduct


class DatabaseConnection:
    #def __init__(self):
    #    try:
    #        self.connection = psycopg2.connect(
    #            dbname="shopping",
    #            user="lolo",
    #            password="cestmoi",
    #            host="localhost"
    #        )
    #        self.connection.autocommit = True
    #        self.cur = self.connection.cursor()
    #    except:
    #        print("cannot connect to database shopping")

    @staticmethod
    def create_tables():
        Purchase.create()
        Store.create()
        Product.create()
        PurchaseStore.create()
        PurchaseProduct.create()
        StoreProduct.create()

    #def insert_data(self):
    #    sql = """INSERT INTO store(name, number) VALUES(%s, %s);"""
    #    data = [("intermarche", 12), ("auchan", 45)]
    #    self.cur.executemany(sql, data)


if __name__ == "__main__":
    #base = DatabaseConnection()
    DatabaseConnection.create_tables()
    #base.insert_data()

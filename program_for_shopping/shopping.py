import psycopg2
from create_tables import CreateTables
from purchase import Purchase


class Shopping:

    def __init__(self):
       CreateTables()

    @staticmethod
    def insert_datas():
        purchase = Purchase()
        purchase.record_purchase()


if __name__ == "__main__":
    shopping = Shopping()
    shopping.insert_datas()

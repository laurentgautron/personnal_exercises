import psycopg2
from create_tables import CreateTables
from purchase import Purchase


class Shopping:

    def __init__(self):
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql_init = """ALTER DATABASE shopping SET datestyle TO 'ISO, DMY';"""
        cur.execute(sql_init)
        conn.commit()
        cur.close()
        conn.close()
        CreateTables()

    @staticmethod
    def insert_datas():
        purchase = Purchase()
        purchase.record_purchase()


if __name__ == "__main__":
    shopping = Shopping()
    shopping.insert_datas()

from create_tables import CreateTables
from record import Record


class Shopping:

    def __init__(self):
        CreateTables()

    @staticmethod
    def insert_datas():
        record = Record()
        record.record_purchase()


if __name__ == "__main__":
    shopping = Shopping()
    shopping.insert_datas()

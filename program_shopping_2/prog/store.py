from connection import Connection
from check import Check

class Store:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS store(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        road VARCHAR(100),
                        road_number VARCHAR(100),
                        town VARCHAR(100),
                        postcode INT,
                        bank_name VARCHAR(100));"""
                        )

    @staticmethod
    def store_last_id():
        with Connection.get_cursor() as cur:
            cur.execute("SELECT MAX(id) FROM store;")
            store_last_id = cur.fetchone()
        return store_last_id

    @staticmethod
    def record_store():
        name = input("entrez le nom du magasin: ")
        road = input("entrez le nom de la rue: ")
        road_number = input("entrez le numéro de la rue: ")
        town = input("entrez le nom de la ville: ")
        postcode = Check.check_postcode()
        bank_name = input("entrez (si vous le connaissez) le nom bancaire du magasin: ")
        sql = ("""INSERT INTO store(name, road, road_number, town, postcode, bank_name)
                values(%s, %s, %s, %s, %s, %s);""")
        with Connection.get_cursor() as cur:
            cur.execute(sql, (name, road, road_number, town, postcode, bank_name))
        store_id = Store.store_last_id()
        return store_id

    @staticmethod
    def store_chearch(store_name):
        print("le type de store_name est: ", type(store_name))
        with Connection.get_cursor() as cur:
            cur.execute("SELECT * FROM store WHERE store.name = %s;", (store_name, ))
            store_list = cur.fetchall()
        return store_list

    @staticmethod
    def get_store(sentence):
        store_name = input(sentence)
        print(store_name, type(store_name))
        store_list = Store.store_chearch(store_name)
        if not store_list:
            print("pas de magasins à ce nom")
        else:
            Display.display_store(store_list)
            store_choice = Check.check_choice_list("choissez un nmagasin parmi la liste proposée ou bien quittez (q )")
        if (not store_list) or (store_choice == 'q'):
            store_id = Store.record_store()
        return store_id

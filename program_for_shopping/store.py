import psycopg2


class Store:

    @staticmethod
    def find_store(store_name):
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT * FROM store WHERE store_name = %s", (store_name, ))
        rows = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        store_attribute = False
        if not rows:
            print('nouveau magasin! ')
        else:
            for indice, row in enumerate(rows):
                print(indice + 1, end=" ")
                for i in range(1, 6):
                    print(row[i], end=" ")
                print()
            choice = input('choisissez un magasin (taper 0 si nouveau) ')
            if choice != '0':
                store_attribute = rows[choice]
            else:
                store_attribute = False
        return store_attribute

    def insert_menu(self):
        store_name = input('quel est le nom du magasin? ')
        store_attribute = self.find_store(store_name)
        if not store_attribute:
            print('son adresse')
            road = input('nom de la rue: ')
            road_number = input('numéro de la rue: ')
            city = input('nom de la ville: ')
            postcode = input('code postal: ')
            store_attribute = store_name, road_number, road, city, postcode
        return store_attribute

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS store (
                        store_id serial PRIMARY KEY,
                        store_name VARCHAR(100),
                        road_number INT,
                        road VARCHAR(100),
                        city VARCHAR(100),
                        postcode INT);"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO store(store_name, road_number, road, city, postcode) VALUES (%s, %s, %s, %s, %s)"""
        menu_datas = self.insert_menu()
        cur.execute(sql_insert, menu_datas)
        conn.commit()
        cur.close()
        conn.close()
        return menu_datas[0]

import psycopg2


class Store:

    @staticmethod
    def find_store_id(store_name):
        conn = psycopg2.connect(dbname="shopping", user="lolo", password="cestmoi", host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT store_id FROM store WHERE store_name = %s", (store_name, ))
        result = cur.fetchone()
        return result

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
            choice = int(input('choisissez un magasin (taper 0 si nouveau) '))
            if choice != 0:
                store_attribute = rows[choice-1]
            else:
                store_attribute = False
        return store_attribute

    @staticmethod
    def insert(store_attribute):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO store(store_name, road_number, road, city, postcode) VALUES (%s, %s, %s, %s, %s)"""
        cur.execute(sql_insert, store_attribute)
        conn.commit()
        cur.close()
        conn.close()

    def insert_store(self):
        store_name = input('quel est le nom du magasin? ')
        store_id = self.find_store(store_name)
        if not store_id:
            print('son adresse')
            road = input('nom de la rue: ')
            road_number = input('numéro de la rue: ')
            city = input('nom de la ville: ')
            postcode = input('code postal: ')
            store_attribute = (store_name, road_number, road, city, postcode)
            self.insert(store_attribute)
            store_id = self.find_store_id(store_attribute[0])
        return store_id[0]

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



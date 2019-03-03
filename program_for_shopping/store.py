import psycopg2


class Store:

    @staticmethod
    def insert_menu():
        store_name = input('quel est le nom du magasin? ')
        print('son adresse')
        road = input('nom de la rue: ')
        road_number = input('numérde la rue: ')
        city = input('nom de la ville: ')
        postcode = input('code postal: ')
        return store_name, road_number, road, city, postcode

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
        cur.execute(sql_insert, self.insert_menu())
        conn.commit()
        cur.close()
        conn.close()

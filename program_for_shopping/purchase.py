import psycopg2
from datetime import datetime


class Purchase:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase (purchase_id serial PRIMARY KEY, date DATE, 
                        time TIME[0], total_price DECIMAL(4,2), nb_article INT)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    @staticmethod
    def insert():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        data = []
        data[0] = input('rentrer le nom du magasin: ')
        date_choice = input('garder la date du jour (y/n)? ')
        if date_choice == 'y':
            data[1] = str(datetime.today().strftime('%d/%m/%Y'))
        else:
            data[1] = input('Entrer la date (jj/mm/aaaa) ')
        data[2] = input('quelle heure? ')

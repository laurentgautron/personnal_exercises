import psycopg2
from datetime import datetime


class Purchase:

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase (purchase_id serial PRIMARY KEY, date DATE, 
                        purchase_time TIME, total_price DECIMAL(4,2), nb_article INT)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    @staticmethod
    def insert():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        date_choice = input('garder la date du jour (y/n)? ')
        if date_choice == 'y':
            date_achat = (str(datetime.today().strftime('%d/%m/%Y')))
        else:
            date_achat = input('Entrer la date (jj/mm/aaaa) ')
            date_achat = datetime.strftime(datetime.strptime(date_achat, '%d%m%Y'), '%d/%m/%Y')
        heure = input('quelle heure (HHMMSS)? ')
        heure =datetime.strftime(datetime.strptime(heure, '%H%M%S'), '%H:%M:%S')
        prix = float(input('le prix total des courses (dans ce magasin) ? ').replace(',', '.'))
        articles = int(input('nombre d\'articles achetés? '))
        datas = (date_achat, heure, prix, articles)
        sql = """INSERT INTO purchase (date, purchase_time, total_price, nb_article) VALUES (%s, %s, %s, %s)"""
        cur.execute(sql, (date_achat, heure, prix, articles))
        conn.commit()
        cur.close()
        conn.close()

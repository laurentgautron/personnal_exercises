import os
import psycopg2
from datetime import datetime
from ask import Ask
from store import Store
from pruchase_store import PurchaseStore
from product import Product
from last import Last


class Purchase:

    def __init__(self):
        self.store = Store()
        self.purchase_store = PurchaseStore()
        self.product = Product()
        self.purchase = Purchase()

    def insert_menu(self):
        date_choice = Ask.ask_string('garder la date du jour ? ', True)
        if date_choice == 'o':
            date_achat = (str(datetime.today().strftime('%d/%m/%Y')))
        else:
            date_achat = input('Entrer la date (jj/mm/aaaa) ')
            date_achat = datetime.strftime(datetime.strptime(date_achat, '%d%m%Y'), '%d/%m/%Y')
        heure = input('quelle heure (HHMMSS)? ')
        heure = datetime.strftime(datetime.strptime(heure, '%H%M%S'), '%H:%M:%S')
        prix = float(input('le prix total des courses (dans ce magasin) ? ').replace(',', '.'))
        articles = int(input('nombre d\'articles achetés? '))
        carte_code = input('le code de la carte utilisée:')
        return date_achat, heure, prix, articles, carte_code

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS purchase (
                        purchase_id serial PRIMARY KEY,
                        date DATE,
                        purchase_time TIME,
                        total_price DECIMAL(5,2),
                        nb_article INT,
                        carte_code INT)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql = """INSERT INTO purchase (date, purchase_time, total_price, nb_article, carte_code) 
                 VALUES (%s, %s, %s, %s, %s)"""
        menu_datas = self.insert_menu()
        cur.execute(sql, menu_datas)
        conn.commit()
        cur.close()
        conn.close()
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql = """SELECT purchase_id FROM purchase
               WHERE purchase_id = (SELECT MAX(purchase_id) FROM purchase) """
        cur.execute(sql)
        last_purchase_id = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return last_purchase_id, menu_datas[3], menu_datas[0], menu_datas[1]

    def record_purchase(self):
        purch = 'o'
        while purch == 'o':
            if os.path.isfile('list_record.json'):
                last_purchase, nb_articles, last_article, store = Last.display_last_datas()
            else:
                last_purchase, nb_articles, day, hour = self.purchase.insert()
                store = self.store.insert_store()
                self.purchase_store.insert(last_purchase, store)
            self.product.record_product(last_purchase, nb_articles, day, hour)
            purch = input('enregistrer un autre achat (o/n)? ')



import json
import os
import psycopg2
from datetime import datetime
from ask import Ask
from store import Store
from purchase_store import PurchaseStore
from product import Product
from last import Last


class Purchase:

    def __init__(self):
        self.store = Store()
        self.purchase_store = PurchaseStore()
        self.product = Product()

    @staticmethod
    def insert_menu():
        date_choice = Ask.ask_string('garder la date du jour ? ', yn=True)
        if date_choice == 'o':
            date_purchase = (datetime.today().strftime('%d/%m/%Y'))
        else:
            date_purchase = Ask.ask_number('Entrer la date (jj/mm/aaaa) ', day=True)
        heure = Ask.ask_number('quelle heure (HHMMSS)? ', hour=True)
        prix = Ask.ask_number('le prix total des courses (dans ce magasin) ? ', price=True)
        articles = Ask.ask_number('nombre d\'articles achetés? ', nbarticle=True)
        carte_code = Ask.ask_number('le code de la carte utilisée:', code=True)
        return date_purchase, heure, prix, articles, carte_code

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

    @staticmethod
    def insert():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql = """INSERT INTO purchase (date, purchase_time, total_price, nb_article, carte_code) 
                 VALUES (%s, %s, %s, %s, %s);"""
        menu_datas = Purchase.insert_menu()
        print(menu_datas)
        cur.execute(sql, menu_datas)
        conn.commit()
        cur.close()
        conn.close()
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        sql_max_id = """SELECT purchase_id FROM purchase
               WHERE purchase_id = (SELECT MAX(purchase_id) FROM purchase) """
        cur.execute(sql_max_id)
        last_purchase_id = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return last_purchase_id, menu_datas[3], menu_datas[0], menu_datas[1]

    def record_purchase(self):
        purch = 'o'
        while purch == 'o':
            if os.path.isfile('list_record.json'):
                last_purchase, last_article, store, nb_articles, day, hour = Last.display_last_datas()
                os.remove('list_record.json')
            else:
                last_purchase, nb_articles, day, hour = Purchase.insert()
                store = self.store.insert_store()
                self.purchase_store.insert(last_purchase, store)
            print(last_purchase, nb_articles, store, day, hour)
            self.product.record_product(last_purchase, nb_articles, store, day, hour)
            purch = Ask.ask_string('enregistrer un autre achat (o/n)? ', yn=True)

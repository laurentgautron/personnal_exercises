import os
import psycopg2
from tables import Tables
from menu_first import Menu

class Shopping:

    def __init__(self):
        con = psycopg2.connect(dbname="postgres", user='laurentg', password="")
        print("Database opened successfully")
        con.autocommit = True
        cur = con.cursor()
        cur.execute("DROP DATABASE IF  EXISTS lolo;")
        cur.execute("""CREATE DATABASE lolo;""")
        cur.close()
        con.close()
        Tables.create()

    def menu(self):
        os.system('clear')
        while True:
            choice = Menu.display()
            if choice == 1:
                print("vous voulez terminer un achat en cours")
            elif choice == 2:
                print(" vous voulez enregistrer un achat")
            elif choice == 3:
                print(" vous voulez explorer les donnée enregistrée en base")
            else:
                print("vous nous quittez , à bientôt")
                break

if __name__ == "__main__":
    shopping = Shopping()
    shopping.menu()

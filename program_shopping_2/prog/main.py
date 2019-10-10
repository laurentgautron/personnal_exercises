import os
import psycopg2
from tables import Tables
from menu_first import Menu
from connection import Connection
from database import Database
from record import Record

class Shopping:

    def __init__(self):
        Database.create()
        Tables.create()

    def menu(self):
        os.system('clear')
        while True:
            choice = Menu.display()
            if choice == 1:
                print("vous voulez terminer un achat en cours")
                Record.record()
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

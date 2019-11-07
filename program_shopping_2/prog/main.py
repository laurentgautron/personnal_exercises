import os
import psycopg2
from tables import Tables
from menu import Menu
from database import Database
from purchase import Purchase
from purchase_product import Purchase_product

class Shopping:

    def __init__(self):
        Database.create()
        Tables.create()

    @staticmethod
    def menu():
        os.system('clear')
        while True:
            choice = Menu.display_menu(sentence="votre choix: ", menu="first")
            if choice == "voir les achats en cours":
                print("vous voulez voir les achats en cours d'enregistrement")
                Purchase.false_purchase()
            elif choice == "commencer un achat":
                print(" vous voulez enregistrer un achat")
                Purchase.record_purchase_product()
            elif choice == "explorer des données":
                print(" vous voulez explorer les donnée enregistrée en base")
            else:
                print("vous nous quittez , à bientôt")
                break

if __name__ == "__main__":
    shopping = Shopping()
    shopping.menu()

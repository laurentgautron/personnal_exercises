#from database import Database
from menu_first import Menu

class Shopping:

    #def __init__(self):
    #    Database.create()

    @staticmethod
    def menu():
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
    Shopping.menu()

#from database import Database
from menu_first import Menu

class Shopping:

    #def __init__(self):
    #    Database.create()

    @staticmethod
    def menu():
        choice = Menu.display()
        print(choice)

if __name__ == "__main__":
    Shopping.menu()

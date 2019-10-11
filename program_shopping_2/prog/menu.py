import os
from display import Display

class Menu:

    LIST_FIRST_MENU = ["voir les achats en cours", "commencer un achat",
                       "explorer des données", "quitter le programme"]

    FALSE_PURCHASE_LIST = ["continuer", "supprimer", "abandonner"]

    @staticmethod
    def display_menu(sentence="", menu=""):
        list_menu = list()
        if menu == "first":
            list_menu = __class__.LIST_FIRST_MENU
        elif menu == "second":
            list_menu = __class__.FALSE_PURCHASE_LIST
        Display.display(list_menu)
        max = len(list_menu)
        while True:
            choice = input(sentence)
            try:
                int(choice)
            except ValueError:
                print("vous devez choisir un chiffre entier entre 1 et %s" %max)
            else:
                if int(choice) not in range(1, len(list_menu)+1):
                    print(" ce chiffre ne fait pas parti des choix possibles")
                else:
                    break
        return list_menu[int(choice)-1]

import os
from display import Display
from check import Check

class Menu:

    LIST_FIRST_MENU = ["voir les achats en cours", "commencer un achat",
                       "explorer des données", "quitter le programme"]

    FALSE_PURCHASE_LIST = ["continuer", "supprimer", "abandonner"]

    @staticmethod
    def display_menu(menu, sentence):
        list_menu = list()
        if menu == "first":
            list_menu = __class__.LIST_FIRST_MENU
        elif menu == "second":
            list_menu = __class__.FALSE_PURCHASE_LIST
        Display.display(list_menu)
        choice = Check.check_choice_list(list_menu, sentence)
        return choice

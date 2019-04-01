import os

class Ask:

    @staticmethod
    def ask_liste(liste):
        choice = len(liste) + 1
        while choice not in range(1, len(list) + 1):
            os.system('clear')
            choice = input('rentrer un nombre parmi la liste qui s\'affiche ou 0 pour enregistrer un nouvel élément')
            display(liste)
        return choice

    @staticmethod
    def ask_string(question, yn = False):
        if yn:
            choice = 'a'
            while choice not in ('o', 'n'):
                choice = input(question + (' répondez oui(o) ou non(n) '))
        else:
            choice = input(question)
        return choice

    @staticmethod
    def ask_price_weight_quatity(question, price=False, weight=False, price=False):
        cas price = True:
            try float(input(question).replace(',', '.')):

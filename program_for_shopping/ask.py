import os
from check import Check


class Ask:

    def ask_liste(self, question, liste):
        no_choosed = True
        choice = ''
        while no_choosed:
            choice = input(question)
            display(liste)
            try:
                int(choice)
            except ValueError:
                new_item = self.ask_string('vous voulez rajouter ' + choice + 'dans la liste? ', yn=True)
                if new_item:
                    no_choosed = False
                    # new in list(choice)
            else:
                while choice not in range(1, len(liste) + 1):
                    os.system('clear')
                    choice = input('rentrer un nombre parmi la liste qui s\'affiche ou 0 pour enregistrer \
                     un nouvel élément')
        return choice

    @staticmethod
    def ask_string(question, yn=False):
        if yn:
            choice = 'a'
            while choice not in ('o', 'n'):
                choice = input(question + ' répondez oui(o) ou non(n) ')
            return choice

    @staticmethod
    def ask_number(question, nb=False, weight=False, price=False, day=False, hour=False, code=False):
        while True:
            choice = input(question)
            os.system('clear')
            if nb and Check.nb(choice):
                print('bon nombre? ', Check.nb(choice))
                return int(choice)
            elif weight and Check.weight(choice):
                choice = choice.replace(',', '.')
                print('bon poids? ', Check.weight(choice))
                return float(choice)
            elif price and Check.price(choice):
                choice = choice.replace(',', '.')
                print('bon prix? ', Check.price(choice))
                return float(choice)
            elif hour and Check.hour(choice):
                print('bonne heure? ', Check.hour(choice))
                return choice
            elif day and Check.day(choice):
                print('bonne date? ', Check.day(choice))
                return choice
            elif code and Check.code(choice):
                print('bon code? ', Check.code(choice))
                return int(choice)

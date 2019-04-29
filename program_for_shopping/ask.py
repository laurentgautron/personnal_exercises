import os
from datetime import datetime, date


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
        else:
            choice = input(question)
            return choice

    @staticmethod
    def ask_number(question, nbarticle=False, weight=False, price=False, way_number=False, day=False, hour=False, code=False):
        while True:
            if nbarticle or way_number:
                choice = input(question)
                try:
                    int(choice)
                except ValueError:
                    print("entrer un nombre entier ")
                else:
                    return int(choice)
            elif weight:
                choice = input(question)
                try:
                    float(choice)
                except ValueError:
                    print('vous devez rentrer un nombre pour le poids')
                else:
                    if (float(choice)*1000).is_integer():
                        return float(choice)
                    else:
                        print('seulement 3 chiffres après la virgule')
            elif price:
                choice = input(question)
                try:
                    float(choice)
                except ValueError:
                    print('vous devez rentrer un prix pour cet achat')
                else:
                    c = float(choice) - int(float(choice))
                    print(c)
                    print(c*100 < 1)
                    if (not c*100 < 1) or len(str(int(float(choice)))) > 3:
                        print("""seulement trois chiffres avant une éventuelle virgule et deux chiffres autorisés après
                              la virgule si besoin""")
                    else:
                        return float(choice)
            elif hour:
                choice = input(question)
                try:
                    choice = datetime.strptime(choice, '%H%M%S')
                except ValueError:
                    print('ce n\'es pas un bon type d\'heure')
                else:
                    return choice.time()
            elif day:
                choice = input(question)
                if len(choice) < 9:
                    try:
                        choice = int(choice)
                    except ValueError:
                        print('la date que vous avez rentrée n\'est pas une date correcte !')
                    else:
                        print(choice)
                        return choice
                else:
                    print('il faut rentrer une série de 8 chiffres: (JJMMAAAA)')
            elif code:
                choice = input(question)
                try:
                    int(choice)
                except ValueError:
                    print('vous devez entrer un entier de 4 chiffres (les 4 derniers chiffres de la carte utilisée')
                else:
                    if len(choice) > 4:
                        print(' seulement 4 chiffres (les derniers chiffres de la carte utilisée) ')
                    else:
                        return int(choice)

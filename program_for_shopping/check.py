from datetime import datetime

class Check:

    @staticmethod
    def nb(choice):
        try:
            int(choice)
        except ValueError:
            print("entrer un nombre entier ")
            return False
        return True

    @staticmethod
    def weight(choice):
        try:
            float(choice)
        except ValueError:
            print('vous devez rentrer un nombre pour le poids')
            return False
        else:
            if (float(choice) * 1000).is_integer():
                return True
            else:
                print('seulement 3 chiffres après la virgule')
                return False

    @staticmethod
    def price(choice):
        try:
            float(choice)
        except ValueError:
            print('vous devez rentrer un prix pour cet achat')
            return False
        else:
            if (not (float(choice) * 100).is_integer()) or len(str(int(float(choice)))) > 3:
                print("seulement trois chiffres avant une éventuelle virgule, "
                      "et deux chiffres autorisés après la virgule si besoin")
                return False
            else:
                return True

    @staticmethod
    def hour(choice):
        try:
            datetime.strptime(choice, '%H%M%S')
        except ValueError:
            print('ce n\'es pas un bon type d\'heure')
            return False
        else:
            return True

    @staticmethod
    def day(choice):
        if len(choice) < 9:
            try:
                int(choice)
            except ValueError:
                print('la date que vous avez rentrée n\'est pas une date correcte !')
                return False
            else:
                return True
        else:
            print('il faut rentrer une série de 8 chiffres: (JJMMAAAA)')
            return False

    @staticmethod
    def code(choice):
        try:
            int(choice)
        except ValueError:
            print('vous devez entrer un entier de 4 chiffres (les 4 derniers chiffres de la carte utilisée')
            return False
        else:
            if len(choice) > 4:
                print(' seulement 4 chiffres (les derniers chiffres de la carte utilisée) ')
                return False
            else:
                return True

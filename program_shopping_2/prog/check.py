import datetime

class Check:

    @staticmethod
    def check_choice_list(list_menu, sentence):
        max = len(list_menu)
        while True:
            print(sentence)
            choice = input()
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

    @staticmethod
    def check_yn(sentence):
        while True:
            rep = input(sentence)
            if rep not in ('o','n'):
                print("répondez par oui(taper o) ou non(tapez n)")
            else:
                break
        return rep

    @staticmethod
    def check_cardcode(sentence):
        while True:
            card_code = input(sentence)
            try:
                int(card_code)
            except ValueError:
                print('vous devez rentrer un nombre')
            else:
                if len(card_code) > 4:
                    print('rentrez un nombre entier de 4 chiffres')
                else:
                    break
        return int(card_code)

    @staticmethod
    def check_date(sentence):
        while True:
            date = input(sentence)
            try:
                datetime.datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print("vous n'avez pas rentré un bon format de date")
            else:
                break
        return datetime.datetime.strptime(date, "%d/%m/%Y").date()

    @staticmethod
    def check_hour(sentence):
        while True:
            hour = input(sentence)
            try:
                datetime.datetime.strptime(hour, "%H:%M")
            except ValueError:
                print("vous n'avez pas rentré une bonne heure")
            else:
                break
        return datetime.datetime.strptime(hour, "%H:%M").time()
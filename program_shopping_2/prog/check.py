import datetime

class Check:

    @staticmethod
    def check_choice_list(list_menu, sentence):
        max = len(list_menu)
        while True:
            print(sentence, end=" ")
            choice = input()
            if choice == 'q':
                break
            try:
                int(choice)
            except ValueError:
                print("vous devez choisir un chiffre entier entre 1 et %s ou bien quitter ( q )" %max)
            else:
                if int(choice) not in range(1, len(list_menu)+1):
                    print(" cette réponse ne fait pas parti des choix possibles")
                else:
                    choice = list_menu[int(choice)-1]
                    break
        return choice

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
            len_size = ""
            card_code = input(sentence)
            if len(card_code) != 4:
                len_size = "rentrez les 4 derniers chiffres de la carte"
            try:
                int(card_code)
            except ValueError:
                print("vous devez rentrer un nombre")
            else:
                print(len_size)
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

    @staticmethod
    def check_postcode():
        while True:
            postcode = input("entrez le code postal de la ville ( un nombrre entier composé de 5 chiffres): ")
            try:
                int(postcode)
            except ValueError:
                print("ceci n'est pas un nombre entier")
            else:
                if len(postcode) > 5:
                    print("ce nombre entier a plus de 5 chiffres , ce n'est pas un code postal (français)")
                else:
                    break
        return postcode

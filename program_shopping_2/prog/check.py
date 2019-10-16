

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
            if rep not in ('y','n'):
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
            else
                if len(card_code) > 4:
                    print('rentrez un nombre entier de 4 chiffres')
                else:
                    break
        return int(card_code)

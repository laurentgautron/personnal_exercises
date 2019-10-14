

class Check:

    @staticmethod
    def check_choice(list_menu, sentence):
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

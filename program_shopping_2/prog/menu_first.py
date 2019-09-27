import os

class Menu:

    @staticmethod
    def display():
        list_menu = ["terminer un achat en cours", "commencer un achat",
                     "explorer des données", "quitter le programme"]
        while True:
            for ind, elmt in enumerate(list_menu):
                print(ind + 1, " - " + elmt)
            choice = input("votre choix: ")
            os.system('clear')
            try:
                int(choice)
            except ValueError:
                print("vous devez choisir un chiffre entier entre 1 et 4")
            else:
                if int(choice) not in range(1, len(list_menu)+1):
                    print(" ce chiffre ne fait pas parti des choix possibles")
                else:
                    break
        return int(choice)

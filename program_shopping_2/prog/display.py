from check import Check

class Display:

    @staticmethod
    def display(list_menu):
        for ind, elmt in enumerate(list_menu):
            print(ind + 1, " - " + elmt)

    @staticmethod
    def display_values(values_list, sentence):
        for ind, elmt in enumerate(values_list):
            print(ind+1, " - ", end="")
            elmt = elmt[2:]
            print(elmt, sep=", ")
        choice = Check.check_choice_list(values_list, sentence)
        print("vous avez choisi: " + ' ', choice)
        return choice

    @staticmethod
    def display_store(store_list):
        for ind, elmt in enumerate(store_list):
            print("l'adresse du magasin n° %s est: " %ind)
            print(elmt)
            for store in elmt:
                print("nom: %s" %store(1))
                print("rue: %s" %store(2))
                print("numéro de la rue: %s" %store(3))
                print("ville: %s" %store(4))
                print("code postale: %s" %store(5))
                print("le nom bancaire est: %s" %store(6))

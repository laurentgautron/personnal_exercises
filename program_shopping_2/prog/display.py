from check import Check

class Display:

    @staticmethod
    def display_dict(dict):
        for indice,item in enumerate(dict):
            print(indice+1, '-', item)

    @staticmethod
    def display(list_menu):
        for ind, elmt in enumerate(list_menu):
            print(ind + 1, " - " + elmt)

    @staticmethod
    def display_values(values_list, sentence):
        for ind, elmt in enumerate(values_list):
            print(ind+1, " - ", end="")
            elmt = elmt[1:]
            print(elmt, sep=", ")
        choice = Check.check_choice_list(values_list, sentence)
        print("vous avez choisi: " + ' ', choice)
        return choice

    @staticmethod
    def display_store(store_list):
        for ind, elmt in enumerate(store_list):
            print("l'adresse du magasin n° %s est: " %str(ind+1))
            print("nom: %s" %elmt[1])
            print("rue: %s" %elmt[2])
            print("numéro de la rue: %s" %elmt[3])
            print("ville: %s" %elmt[4])
            print("code postale: %s" %elmt[5])
            print("le nom bancaire est: %s" %elmt[6])

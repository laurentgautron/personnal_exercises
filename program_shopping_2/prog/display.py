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

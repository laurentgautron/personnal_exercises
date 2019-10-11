
class Display:

    @staticmethod
    def display(list_menu):
        for ind, elmt in enumerate(list_menu):
            print(ind + 1, " - " + elmt)

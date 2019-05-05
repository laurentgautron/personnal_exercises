class Check:

    @staticmethod
    def nb(choice):
        try:
            int(choice)
        except ValueError:
            print("entrer un nombre entier ")
            return False
        return True

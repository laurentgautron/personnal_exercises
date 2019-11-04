import json
from check import Check

class Cat:

    @staticmethod
    def check_choice_cat_list(word_list, sentence):
        while True:
            choice = input(sentence)
            if choice =='n':
                break
            try:
                int(choice)
            except ValueError:
                print("vous devez rentre un chiffre entre 1 et %s" %len(word_list))
            else:
                if int(choice) not in range(1, len(word_list)+1):
                    print("ce choix n'est pas dans la liste")
                else:
                    choice = word_list[int(choice) -1]
                    break
        return choice



    @staticmethod
    def display_cat(list_to_display, great_category=None, category=None, sub_category=None):
        print("la great_category dans display-cat: ", great_category)
        word_list = []
        if great_category:
            for indice, key in enumerate(list_to_display.keys()):
                word_list.append(key)
                print(indice+1, '-', key)
            print("choisissez une super catégorie")
        elif category:
            for indice, value in enumerate(list_to_display[great_category]):
                print(indice+1, '-', value)
                word_list.append(value)
            print("choisissez une categorie")
        elif sub_category:
            for indice, value in enumerate(list_to_display[great_category][category]):
                print(indice+1, '-', value)
                word_list.append(value)
            print("choisissez une sous_catégorie")
        cat_choice = Cat.check_choice_cat_list(word_list, "choisissez parmi la liste ou bien tapez (n) pour rajouter à la liste: ")
        return cat_choice

    @staticmethod
    def create(list_to_update, great_category=None, category=None, sub_category=None):
        if great_category:
            cat = input("rentrez la grande catégorie que vous voulez rajouter: ")
            if cat!="nourriture":
                list_to_update[cat] = []
            else:
                list_to_update["nourriture"] = {}
        elif category:
            cat = input("entrez la nouvelle catégorie que voulvoulez rajouter: ")
            list_to_update[great_category][cat] = []
        elif sub_category:
            cat = input("entrez la sou-catégorie que vous voulez rajouter: ")
            list_to_update[great_category][category][cat] = []
        with open("list_categories.json", "w") as cat_file:
            json.dump(list_to_update, cat_file)
        return cat


    @staticmethod
    def choice_cat(great_category=None, category=None, sub_category=None):
        categories_list = None
        with open("list_categories.json", "r") as cat_file:
            list_cat = json.load(cat_file)
        if great_category and list_cat:
            categories_list = list_cat
        elif category and great_category:
            categories_list = list_cat[great_category]
        elif sub_category and category and great_category:
            categories_list = list_cat[great_category][category]
        print("les cat du moment: ", categories_list)
        print("la great categorie dans choice_cat: ", great_category)
        if categories_list:
            cat_choice = Cat.display_cat(list_cat, great_category, category, sub_category)
            if cat_choice != 'n':
                return cat_choice
        else:
            cat_choice = Cat.create(list_cat, great_category, category, sub_category)
            return cat_choice

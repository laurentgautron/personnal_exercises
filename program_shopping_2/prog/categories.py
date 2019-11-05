import json
from display import Display
from check import Check

class Categories:

    @staticmethod
    def choice_list(great_category=None, category=None, rank=1, food=False):
        with open("list_categories.json", 'r') as categories_file:
            categories_list = json.load(categories_file)
        select_list = categories_list
        if categories_list and rank == 1:
            select_list = list(categories_list.keys())
        elif (rank == 2) and (not food):
            select_list = categories_list[great_category]
        elif (rank == 2) and food:
            select_list = list(categories_list[great_category].keys())
        elif rank == 3:
            select_list = categories_list[great_category][category]
        print("la liste est: ", select_list)
        if select_list:
            Display.display(select_list)
            choice = Check.check_choice_list(select_list, "choisssez dans la liste ou bien ajoutez une nouveauté ( tapez n ): ")
        if (not select_list) or (choice == 'n'):
            print("la food dans le choicede cat: ", food)
            choice = Categories.create(categories_list=categories_list,great_category=great_category, category=category,rank=rank)
        print("le choix : ", choice)
        return choice

    @staticmethod
    def create(categories_list, great_category, category, rank):
        if rank == 1:
            name_in_list = input("la liste est complètement vide: rentrez une grande catégorie: ")
            print("le name_in_list:", name_in_list)
            categories_list[name_in_list] = {} if name_in_list=='nourriture' else []
        elif rank == 2:
            name_in_list = input("rentrez l'élément que vous voulez rajouter: ")
            if great_category=='nourriture':
                categories_list[great_category][name_in_list] = []
            else:
                categories_list[great_category].append(name_in_list)
        elif rank == 3:
            name_in_list = input("rentrez un nom d'aliment générique: ")
            categories_list[great_category][category].append(name_in_list)
        with open("list_categories.json", "w") as categories_file:
            json.dump(categories_list, categories_file)
        return name_in_list

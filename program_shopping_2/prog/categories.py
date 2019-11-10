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
            cate_name = 'grande catégorie'
            select_list = list(categories_list.keys())
        elif (rank == 2) and (not food):
            cate_name = 'categorie'
            select_list = categories_list[great_category]
        elif (rank == 2) and food:
            cate_name = 'categorie'
            select_list = list(categories_list[great_category].keys())
        elif rank == 3:
            cate_name = 'sous-categorie'
            select_list = categories_list[great_category][category]
        if select_list:
            Display.display(select_list)
            choice = Check.check_choice_list(select_list, "choisssez une %s dans la liste ou bien ajoutez une nouveauté ( tapez n ): " %cate_name)
            print("le choice des cates dans categories: ", choice)
        if (not select_list) or (choice == 'n'):
            choice = Categories.create(categories_list=categories_list,great_category=great_category, category=category,rank=rank)
        return choice

    @staticmethod
    def create(categories_list, great_category, category, rank):
        if rank == 1:
            name_in_list = input("rentrez une grande catégorie: ")
            categories_list[name_in_list] = {} if name_in_list=='nourriture' else []
        elif rank == 2:
            name_in_list = input("rentrez une catégorie que vous voulez rajouter: ")
            if great_category=='nourriture':
                categories_list[great_category][name_in_list] = []
            else:
                categories_list[great_category].append(name_in_list)
        elif rank == 3:
            name_in_list = input("rentrez un nom d'aliment générique (sous-catégorie): ")
            categories_list[great_category][category].append(name_in_list)
        with open("list_categories.json", "w") as categories_file:
            json.dump(categories_list, categories_file, indent=4)
        return name_in_list

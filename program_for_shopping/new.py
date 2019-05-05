import json
from ask import Ask

class New:

    @staticmethod
    def new_category():
        return input('écrivez la nouvelle catégorie: ')

    @staticmethod
    def new_sub_cat():
        return input('entrez la nouvelle sous_catégorie: ')

    @staticmethod
    def add_a_category(categories, sub_cat, category, new_cat):
        if new_cat:
            categories[category] = [sub_cat]
        else:
            categories[category].append(sub_cat)
        with open('cat.json', 'w') as cat_file:
            json.dump(categories, cat_file, indent=4)

    @staticmethod
    def new_product():
        with open('cat.json', 'r') as file:
            categories = json.load(file)
        new_cat = new_sub_cat = False
        print('nouveau produit !!')
        list_cat = []
        for indice, cat in enumerate(categories):
            list_cat.append(cat)
            print(indice + 1, '-', cat)
        category = Ask.ask_number('choisissez une catégorie (entrer 0 si nouvelle catégorie): ', nb=True)
        if category == 0:
            category = New.new_category()
            sub_cat = New.new_sub_cat()
            new_cat = True
        else:
            category = list_cat[category - 1]
            for indice, sub in enumerate(categories[category]):
                print(indice + 1, '-', sub)
            sub_cat = Ask.ask_number('choisissez une sous-catégorie (entrer 0 si nouvelle): ', nb=True)
            if sub_cat == 0:
                sub_cat = New.new_sub_cat()
                new_sub_cat = True
            else:
                sub_cat = categories[category][sub_cat - 1]
        processed_food = True
        food = Ask.ask_string('est-ce de la nourriture(o,n)? ', yn=True)
        if food == 'o':
            food = True
            transform = Ask.ask_string('la nourriture est-elle transformée (o/n)? ', yn=True)
            if transform == 'n':
                processed_food = False
        else:
            food = False
        if new_sub_cat or new_cat:
            New.add_a_category(categories, sub_cat, category, new_cat)
        return category, sub_cat, food, processed_food

import psycopg2
import json


class Product:

    CATEGORY = ['fruits', 'légumes', 'féculents', 'viandes', 'poissons', 'boulangerie', 'patisserie', 'sucreries',
                'boissons', 'hygiène', 'entretiens', 'chats']
    SUBCATEGORY = ['pommes', 'poires', 'chocolat', 'pain', 'boeuf', 'porc', 'saumon']

    @staticmethod
    def new_sub_category():
        new_sub = input('entrer la nouvelle sous_categorie (taper entrée si nulle): ')
        return new_sub

    def insert_product(self):
        product_name = input('rentrez le nom du produit: ')
        processed_food = True
        transform = input('la nourriture est-elle transformée (o/n)?, ')
        if transform == 'n':
            processed_food = False
        with open('categories.json', 'a') as cat_file:
            categories = json.dumps(cat_file)
        for indice, cat in enumerate(categories):
            print(indice, '-', cat)
        product_category = input('choisissez une catégorie (entrer "n" pour enregistrer une nouvelle): ')
        if product_category == 'n':
            product_category = input('le nom de la nouvelle catégorie: ')
            sub_category = self.new_sub_category()
        else:
            product_category = categories[int(product_category)]
            for indice, value in enumerate(product_category):
                    print(indice, '-', value)
            sub_category = input('choisissez la sous catégorie (taper "n" si c\'est une nouvelle): ')
            if sub_category == 'n':
                sub_category = self.new_sub_category()
        categories[product_category] =
        return product_name, product_category, sub_category, processed_food

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS product (
                        product_id serial PRIMARY KEY,
                        product_name VARCHAR(100),
                        product_category VARCHAR(100),
                        sub_category VARCHAR(100),
                        processed_food BOOLEAN)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

    def insert(self):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO product(product_name, product_category, sub_category, processed_food)
                        VALUES(%s, %s, %s, %s)"""
        cur.execute(sql_insert, self.insert_product())
        conn.commit()
        cur.close()
        conn.close()

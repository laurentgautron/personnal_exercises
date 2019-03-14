import psycopg2
import json


class Product:

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

    def insert_product(self, product_name):
        with open('cat.json', 'r') as file:
            categories = json.load(file)
        new_cat = new_sub_cat = False
        list_cat = []
        for indice, cat in enumerate(categories):
            list_cat.append(cat)
            print(indice + 1, '-', cat)
        category = int(input('choisissez une catégorie (entrer 0 si nouvelle catégorie): '))
        if category == 0:
            category = self.new_category()
            sub_cat = self.new_sub_cat()
            new_cat = True
        else:
            category = list_cat[category - 1]
            for indice, sub in enumerate(categories[category]):
                print(indice + 1, '-', sub)
            sub_cat = int(input('choisissez une sous-catégorie (entrer 0 si nouvelle): '))
            if sub_cat == 0:
                sub_cat = self.new_sub_cat()
                new_sub_cat = True
            else:
                sub_cat = categories[category][sub_cat]
        processed_food = True
        transform = input('la nourriture est-elle transformée (o/n)?, ')
        if transform == 'n':
            processed_food = False
        if new_sub_cat or new_cat:
            self.add_a_category(categories, sub_cat, category, new_cat)
        return product_name, category, sub_cat, processed_food

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

    def insert(self, product_name):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO product(product_name, product_category, sub_category, processed_food)
                        VALUES(%s, %s, %s, %s);"""
        cur.execute(sql_insert, self.insert_product(product_name))
        conn.commit()
        cur.close()
        conn.close()

    def get_last_product(self):
        product_name = input('entrez le nom du produit: ')
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE product.product_name = %s;", (product_name, ))
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if not result:
            print('nouveau produit !!')
            self.insert(product_name)
            conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
            cur = conn.cursor()
            cur.execute("SELECT MAX(product_id) FROM product;")
            result = cur.fetchone()
            product_id = result[0]
            conn.commit()
            cur.close()
            conn.close()
        else:
            product_id = result[0]
        return product_id

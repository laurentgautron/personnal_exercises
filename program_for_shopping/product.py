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

    @staticmethod
    def insert(result):
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_insert = """INSERT INTO product(product_name, product_category, sub_category, processed_food)
                        VALUES(%s, %s, %s, %s);"""
        cur.execute(sql_insert, result)
        conn.commit()
        cur.close()
        conn.close()
        conn = psycopg2.connect(dbname="shopping", user="lolo", password="cestmoi", host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE product_id = (SELECT max(product_id) FROM product);")
        product_id = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return product_id

    def insert_product(self):
        with open('cat.json', 'r') as file:
            categories = json.load(file)
        new_cat = new_sub_cat = False
        product_name = input('entrez le nom du produit: ')
        conn = psycopg2.connect(dbname='shopping', user='lolo', password='cestmoi', host='localhost')
        cur = conn.cursor()
        cur.execute("SELECT product_id FROM product WHERE product.product_name = %s;", (product_name,))
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if not result:
            print('nouveau produit !!')
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
                    sub_cat = categories[category][sub_cat-1]
            processed_food = True
            food = input('est-ce de la nourriture? (o/n)')
            if food == 'o':
                food = True
                transform = input('la nourriture est-elle transformée (o/n)?, ')
                if transform == 'n':
                    processed_food = False
            else:
                food = False
            if new_sub_cat or new_cat:
                self.add_a_category(categories, sub_cat, category, new_cat)
            result = product_name, category, sub_cat,food, processed_food
            product_id = self.insert(result)
        else:
            product_id = result[0]
        return product_id

    @staticmethod
    def create():
        conn = psycopg2.connect(dbname="shopping", user="lolo", host="localhost", password="cestmoi")
        cur = conn.cursor()
        sql_create = """CREATE TABLE IF NOT EXISTS product (
                        product_id serial PRIMARY KEY,
                        product_name VARCHAR(100),
                        product_category VARCHAR(100),
                        sub_category VARCHAR(100),
                        food BOOLEAN,
                        processed_food BOOLEAN)"""
        cur.execute(sql_create)
        cur.close()
        conn.commit()
        conn.close()

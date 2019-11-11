import json
from connection import Connection
from categories import Categories
from check import Check
from display import Display

class Product:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS product (
                        id SERIAL PRIMARY KEY,
                        product_name VARCHAR(100),
                        great_category VARCHAR(100),
                        category VARCHAR(100),
                        sub_category VARCHAR(100),
                        processed_food BOOLEAN,
                        conditionned_weight DECIMAL(7,2) DEFAULT None);"""
                        )

    @staticmethod
    def cond_weight():
        weight = None
        cond = Check.check_yn("est-ce un produit conditionné (o/n)? ")
        if cond == 'o':
            weight = Check.check_weight_price("entrez le poids conditionné : ", weight=True)
        return weight

    @staticmethod
    def new_product(product_name):
        processed_food = food = False
        conditionned_weight = sub_category = category = great_category = None
        print("pour le new product gret, category  et sub: ", great_category, category, sub_category)
        great_category = Categories.choice_list(rank=1)
        if great_category == 'r':
            print("vous devez choisir une grande catégorie !")
            Product.new_product(product_name)
        elif great_category != "nourriture":
            category = Categories.choice_list(great_category=great_category, rank=2)
            if category == 'r':
                Product.new_product(product_name)
        else:
            category = Categories.choice_list(great_category=great_category, rank=2, food=True)
            if category == 'r':
                Product.new_product(product_name)
            else:
                sub_category = Categories.choice_list(great_category=great_category, category=category, rank=3)
                if sub_category == 'r':
                    Product.new_product(product_name)
                else:
                    conditionned_weight = Product.cond_weight()
                    rep = Check.check_yn("Est_ce de la nourriture transformée? ")
                    if rep == "o":
                        processed_food = True
        datas = product_name, great_category, category, sub_category, processed_food, conditionned_weight
        with Connection.get_cursor() as cur:
            sql = ("""INSERT INTO product(product_name, great_category, category, sub_category, processed_food, conditionned_weight)
                   VALUES (%s, %s, %s, %s, %s, %s);""")
            cur.execute(sql, datas)
        with Connection.get_cursor() as cur:
            cur.execute("SELECT MAX(id) FROM product")
            product_id = cur.fetchone()
        return product_id[0], conditionned_weight, food

    @staticmethod
    def product_research(product_name):
        with Connection.get_cursor() as cur:
            sql = ("""SELECT * FROM product WHERE product_name = %s;""")
            cur.execute(sql, (product_name,))
            product_list = cur.fetchall()
        return product_list

    @staticmethod
    def product_get_datas(product_name):
        product_id = weight = None
        food = False
        product_list = Product.product_research(product_name)
        if not product_list:
            print(" pas de produit portant ce nom! ")
        else:
            product_choice = Display.display_values(product_list, "choisissez un produit parmi la liste ou bien quittez (q): ")
        if (not product_list) or (product_choice == 'q'):
            new_product = Check.check_yn("voulez-vous enregistrer ce nouveau produit , ")
            if new_product=='o':
                print("vous enregistrez un nouveau produit")
                product_id, weight, food = Product.new_product(product_name)
        else:
            product_id, weight = product_choice[0], product_choice[6]
        return product_id, weight, food

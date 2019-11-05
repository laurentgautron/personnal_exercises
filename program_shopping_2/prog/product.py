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
                        conditionned_weight DECIMAL(7,2) DEFAULT 0.0);"""
                        )

    @staticmethod
    def cond_weight():
        weight = None
        cond = Check.check_yn("est-ce un produit conditionné (o/n)? ")
        if cond == 'o':
            weight = Check.check_weight("entrez le poids conditionné : ")
        return weight

    @staticmethod
    def new_product(product_name):
        processed_food = False
        great_category = Categories.choice_list(rank=1)
        print("la great: ", great_category)
        if great_category != "nourriture":
            category = Categories.choice_list(great_category=great_category, rank=2)
        else:
            print("ça se bouffe")
            category = Categories.choice_list(great_category=great_category, rank=2, food=True)
            sub_category = Categories.choice_list(great_category=great_category, category=category, rank=3)
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
        return product_id[0], conditionned_weight

    @staticmethod
    def product_research(product_name):
        print("le product_name qui existe: ", product_name)
        with Connection.get_cursor() as cur:
            sql = ("""SELECT * FROM product WHERE product_name = %s;""")
            cur.execute(sql, (product_name,))
            product_list = cur.fetchall()
        return product_list

    @staticmethod
    def product_get_datas(product_name):
        product_list = Product.product_research(product_name)
        if not product_list:
            print(" pas de produit portant ce nom! ")
        else:
            Display.display_product(product_list)
            product_choice = Check.check_choice_list(product_list, "choisissez un produit parmi la liste proposée ou bien quittez (q): ")
        if (not product_list) or (product_choice == 'q'):
            product_id, weight = Product.new_product(product_name)
        else:
            product_id, weight = product_choice[6]
        return product_id, weight

from connection import Connection
from cat import Cat

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
                        isfood BOOLEAN DEFAULT False,
                        processed_food BOOLEAN DEFAULT False,
                        conditionned_weight DECIMAL(7,2) DEFAULT 0);"""
                        )

    @staticmethod
    def new_product(product_name):
        great_category = Cat.choice_cat(great_category=True)
        print("mais: ", great_category)
        category = Cat.choice_cat(great_category, category=True)
        if great_category == "nourriture":
            isfood = True
            sub_category, conditionned_weight = Cat.choice_cat(great_category, category, sub_category=True)
            rep = Check.check_yn("Est_ce de la nourriture transformée? ")
            if rep == "o":
                processed_food = True
        datas = product_name, great_category, category, sub_category, isfood, processed_food, conditionned_weight
        with Connection.get_cursor() as cur:
            sql = ("""INSERT INTO product(product_name, great_category, caegory, sub_category, isfood, processed_food, conditionned_weight)
                   VALUES (%s, %s, %s, %s, %s, %s, %s);""")
            cur.execute(sql, datas)

    @staticmethod
    def product_research(product_name):
        print('on a rentré le:', product_name)
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
            product_id, weight = product_data(product_store)
        return product_id, weight

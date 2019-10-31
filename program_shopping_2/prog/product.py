from connection import Connection

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
                        isfood BOOLEAN,
                        processed_food BOOLEAN,
                        coditionnded_weight DECIMAL(7,2)) DEFAULT 0;"""
                        )

    @staticmethod
    def new_product(product_name):


    @staticmethod
    def product_research(product_name):
        with Connection.get_cursor() as cur:
            cur.execute("""SELECT * FROM product WHERE product_name = %s;""" %product_name)
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

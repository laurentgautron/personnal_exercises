from connection import Connection
from product import Product
from check import Check

class Purchase_product:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS purchase_product(
                        id SERIAL PRIMARY KEY,
                        purchase_id INT,
                        product_id INT,
                        price DECIMAL(5,2),
                        weight DECIMAL(7,2));"""
                        )

    @staticmethod
    def purch_pro_get_datas(product_name, food = False):
        product_id, weight = Product.product_get_datas(product_name)
        if weight == None and food:
            weight = Check.check_weight_price("entrez le poids du produit: ", weight=True)
        price = Check.check_weight_price("entrez le prix de l'article", price=True)
        return product_id, price, weight

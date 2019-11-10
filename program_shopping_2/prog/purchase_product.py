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
    def purch_pro_get_datas(product_name, food=False):
        product_id = weight = None
        print("product et weight dans purchpro get datas: ", (product_id, weight))
        print("le food dans purchet pro de purchase_product: ", food)
        product_id, weight, food = Product.product_get_datas(product_name)
        if weight == None and food:
            weight = Check.check_weight_price("entrez le poids du produit: ", weight=True)
        if product_id:
            price = Check.check_weight_price("entrez le prix de l'article: ", price=True)
        else:
            price = None
        return product_id, price, weight

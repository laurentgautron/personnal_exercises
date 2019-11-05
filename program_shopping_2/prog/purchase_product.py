from connection import Connection
from purchase import Purchase
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
    def purch_pro_get_datas(product_name):
        product_id, weight = Product.product_get_datas(product_name)
        if weight == None:
            weight = Check.check_weight("entrez le poids du produit: ")
        price = Check.check_price()
        return product_id, price, weight

    @staticmethod
    def record_purchase_product(purchase_id=None):
        product_name = ""
        rep = ''
        nb_product = 0
        while rep != 'q':
            if purchase_id != None:
                print("le purchase_id du record: ", purchase_id)
                nb_product = Purchase.count_nb_product(purchase_id)
                print("il y a déjà %s produits enregistrés pour cet achat" %nb_product)
            else:
                print ("vous commencez l'enregistrement de l'achat !")
                purchase_id = Purchase.purchase_record()
                print("le purchase: ", purchase_id)
            product_name = input("rentrez le nom d'un produit ou bien 'q' pour quitter: ")
            if product_name=='q':
                break
            product_id, price, weight = Purchase_product.purch_pro_get_datas(product_name)
            datas = (purchase_id, product_id, price, weight)
            print("les datas: ", datas)
            with Connection.get_cursor() as cur:
                sql = ("""INSERT INTO purchase_product(purchase_id, product_id, price, weight)
                       VALUES (%s, %s, %s, %s);""")
                cur.execute(sql, datas)
        stop_record = Check.check_yn("vous arrétez l'enregistrement de produits, avez_vous fini l'enregistrement ?")
        if stop_record == 'o':
            Purchase.purchase_stop(purchase_id, nb_product)

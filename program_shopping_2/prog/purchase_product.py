from connection import Connection
from purchase import Purchase

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
        if purchase_id == None:
            purchase_id = Purchase.purchase_get_data()
        product_id, weight = Product.product_get_datas(product_name)
        if not weight:
            weight = Check.check_weight()
        price = Check.check_price()
        return purchase_id, product_id, price, weight

    @staticmethod
    def record_purchase_product(purchase_id=None):
        product_name = ""
        nb_product = 0
        while rep != 'q':
            if purchase_id != None:
                nb_product = Purchase.count_nb_product(purchase_id)
                print("il y a déjà %s produits enregistrés pour cet achat" %nb_product)
            else:
                print ("vous commencez l'enregistrement de l'achat !")
            product_name = input("rentrez le nom d'un produit ou bien 'q' pour quitter: ")
            with Connection.get_cursor() as cur:
                sql = ("""INSERT INTO purchase_product(purchase_id, product_id, price, weight)
                       VALKUES (%s, %s, %s, %s);""")
                cur.execute(sql, purchase_id, Purchase_record.purch_pro_get_datas(product_name))
        stop_record = Check.check_yn("vous arrétez l'enregistrement de produits, avez_vous fini l'enregistrement ?")
        if stop_record == 'o':
            Purchase.purchase_stop(purchase_id, nb_product)

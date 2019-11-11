import json
from datetime import datetime
from connection import Connection
from display import Display
from menu import Menu
from check import Check
from store import Store
from purchase_product import Purchase_product

class Purchase:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS purchase (
                        id SERIAL PRIMARY KEY,
                        purch BOOLEAN DEFAULT FALSE,
                        date DATE,
                        hour TIME,
                        article_number INT DEFAULT 0,
                        total_price DECIMAL(5,2),
                        card_code INT,
                        store_id INT,
                        today TIMESTAMP DEFAULT now());"""
                        )

    @staticmethod
    def purchase_close(purchase_id, nb_product, total_price):
        with Connection.get_cursor() as cur:
            cur.execute("""UPDATE purchase SET purch=True, article_number=%s, total_price=%s WHERE id =%s; """ %(nb_product, total_price, purchase_id))

    @staticmethod
    def count_nb_product_total_price(purchase_id):
        with Connection.get_cursor() as cur:
            cur.execute("""SELECT COUNT(*), SUM(price) FROM purchase_product WHERE purchase_id = %s;""" %purchase_id)
            count = cur.fetchone()
        return count[0], count[1]

    @staticmethod
    def change_code(card_code, list_card_code):
        Display.display_dict(list_card_code)
        name = Check.check_choice_list(list(list_card_code.keys()), "le nom de la pesonne à qui appartient le code: ")
        list_status = ["compte perso", "compte commun"]
        Display.display(list_status)
        status = Check.check_choice_list(list_status, "de quel compte s'agit-il ? ")
        compte = "commun" if status == "compte commun" else "perso"
        if list_card_code[name][compte]:
            Display.display(list_card_code[name][compte])
            code_to_remove = Check.check_choice_list(list_card_code[name][compte], "supprimez des numéros dans %s de %s: " %(status,name))
            list_card_code[name][compte].remove(code_to_remove)
        list_card_code[name][compte].append(str(card_code))
        with open("card_list_code.json", "w") as file:
            json.dump(list_card_code, file)

    @staticmethod
    def card_code_isfind(list_card_code, card_code, find_personn = False):
        find_someone = False
        for human, values in list_card_code.items():
            for status, codes in values.items():
                for code in codes:
                    if card_code == int(code):
                        personn = human
                        kind_card = status
                        find_someone = True
        if find_personn:
            return personn, kind_card, find_someone
        else:
            return find_someone

    @staticmethod
    def record_purchase_product(purchase_id=None):
        product_name = ""
        rep = ''
        nb_product = 0
        total_price = 0
        product_id = None
        while rep != 'q' or product_id==None:
            if purchase_id != None:
                nb_product, total_price = Purchase.count_nb_product_total_price(purchase_id)
                print("il y a déjà %s produits enregistrés pour cet achat pour un montant de %s euros !" %(nb_product, total_price))
            else:
                print ("vous commencez l'enregistrement de l'achat !")
                purchase_id = Purchase.purchase_record()
            product_name = input("rentrez le nom d'un produit ou bien quittez (taper q): ")
            if product_name=='q':
                break
            product_id, price, weight = Purchase_product.purch_pro_get_datas(product_name)
            print("le product_id dans le purchase.record_purchase_product: ", product_id)
            datas = (purchase_id, product_id, price, weight)
            if product_id != None:
                with Connection.get_cursor() as cur:
                    sql = ("""INSERT INTO purchase_product(purchase_id, product_id, price, weight)
                           VALUES (%s, %s, %s, %s);""")
                    cur.execute(sql, datas)
        stop_record = Check.check_yn("vous arrétez l'enregistrement de produits, avez_vous fini l'enregistrement ? ")
        if stop_record == 'o':
            Purchase.purchase_close(purchase_id, nb_product, total_price)

    @staticmethod
    def purchase_delete(purchase_choice):
        with Connection.get_cursor() as cur:
            cur.execute("DELETE FROM purchase WHERE id = %s;" %purchase_choice)
            cur.execute("DELETE FROM purchase_product WHERE purchase_id = %s;" %purchase_choice)

    @staticmethod
    def false_purchase():
        want_to_continue = True
        while want_to_continue:
            with Connection.get_cursor() as cur:
                cur.execute("""SELECT * FROM purchase WHERE purch = False;""")
                purchase_incourse_list = cur.fetchall()
            if not purchase_incourse_list:
                print("la liste est vide: pas de ticket en cours d'enregistrement")
                want_to_continue = False
            else:
                user_choice = Display.display_values(purchase_incourse_list, "choisissez un élément de la liste: ")
                action_choice = Menu.display_menu(menu="second", sentence="quelle action voulez-vous effectuer sur cet achat ?")
                if action_choice == "continuer":
                    print("vous continuez l'enregistrement de cet achat! ")
                    purchase_id = user_choice[0]
                    Purchase.record_purchase_product(purchase_id)
                elif action_choice == "supprimer":
                    print("vous supprimez cet enregistrement")
                    Purchase.purchase_delete(user_choice[0])
                else:
                    break
                user_pursue = Check.check_yn("voulez-vous poursuivre a consulter les achats en cours ? ")
                if user_pursue=='n':
                    want_to_continue =False

    @staticmethod
    def purchase_get_data():
        store_id = 0
        with open("card_list_code.json", 'r') as card:
            list_card_code = json.load(card)
        today = datetime.today()
        date_choice = Check.check_yn("voulez_vous garder la date et l'heure du jour (o/n)? ")
        if date_choice == 'o':
            date = datetime.today().date()
            hour = datetime.today().time().isoformat(timespec='seconds')
        else:
            date = Check.check_date("enrez la date (jj/mm/YYYY): ")
            hour = Check.check_hour("entrez l'heure (H:M): ")
        while store_id == 0 or store_id =='q':
            store_id = Store.get_store("entrez le nom du magasin: ")
        while True:
            card_code = Check.check_cardcode("entrez le numéro de carte de paiement ( les 4 dernier chiffres de la carte ): ")
            if not Purchase.card_code_isfind(list_card_code, card_code):
                new_card = Check.check_yn("nouvelle carte (o/n)? ")
                if new_card == 'o':
                    Purchase.change_code(card_code, list_card_code)
                    break
            else:
                break
        return date, hour, card_code, today, store_id

    @staticmethod
    def purchase_record():
        with Connection.get_cursor() as cur:
            sql = ("""INSERT INTO purchase(date, hour, card_code, today, store_id)
                      VALUES(%s, %s, %s, %s, %s);""")
            cur.execute(sql, Purchase.purchase_get_data())
        with Connection.get_cursor() as cur:
            cur.execute("SELECT MAX(id) FROM purchase;")
            purchase_id = cur.fetchone()
        return purchase_id[0]

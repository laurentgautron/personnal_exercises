import json
from datetime import datetime
from connection import Connection
from display import Display
from menu import Menu
from check import Check
from store import Store

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
    def purchase_stop(purchase_id, nb_product):
        with Connection.get_cursor() as cur:
            cur.execute("""UPDATE purchase SET purch=True, article_number=0 WHERE id =%s; """ %purchase_id)


    @staticmethod
    def count_nb_product(purchase_id):
        with Connection.get_cursor() as cur:
            cur.execute("""SELECT COUNT(*) FROM purchase_product WHERE purchase_id = %s;""" %purchase_id)

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
    def purchase_delete(purchase_choice):
        with Connection.get_cursor() as cur:
            cur.execute("DELETE FROM purchase WHERE id = %s;" %purchase_choice)

    @staticmethod
    def false_purchase():
        with Connection.get_cursor() as cur:
            cur.execute("""SELECT * FROM purchase WHERE purch = False;""")
            purchase_incourse_list = cur.fetchall()
        if not purchase_incourse_list:
            print("la liste est vide: pas de ticket en cours d'enregistrement")
        while purchase_incourse_list:
            purchase_choice = Display.display_values(purchase_incourse_list, "choisissez un élément de la liste: ")
            action_choice = Menu.display_menu(menu="second", sentence="quelle action voulez-vous effectuer sur cet achat ?")
            if action_choice == "continuer":
                print("vous continuez l'enregistrement de cet achat")
                purchase_id = purchase_incourse_list[choice][0]
                Purchase_product.record_purchase_product(purchase_id)
            elif action_choice == "supprimer":
                print("vous supprimez cet enregistrement")
                Purchase.purchase_delete(purchase_choice[0])
                purchase_incourse_list.remove(purchase_choice)
            else:
                break

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

from connection import Connection
from display import Display
from menu import Menu

class Purchase:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS purchase (
                        id SERIAL PRIMARY KEY,
                        purch BOOLEAN DEFAULT FALSE,
                        date DATE,
                        hour TIME,
                        article_number INT,
                        total_price DECIMAL(5,2),
                        card_code INT,
                        store_id INT);"""
                        )

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
            print(purchase_incourse_list)
            purchase_choice = Display.display_values(purchase_incourse_list, "choisissez un élément de la liste")
            action_choice = Menu.display_menu(menu="second", sentence="quelle action voulez-vous effectuer sur cet achat ?")
            if action_choice == "continuer":
                print("vous continuez l'enregistrement de cet achat")
            elif action_choice == "supprimer":
                print("vous supprimez cet enregistrement")
                Purchase.purchase_delete(purchase_choice[0])
                purchase_incourse_list.remove(purchase_choice)
            else:
                break

    @staticmethod
    def purchase_record():
        date_and_hour_day =
        date_choice = Check.check_yn("voulez_vous garder la date et l'heure du jour ? ")
        if date_choice == 'o':
            date = datejour
            hour = heure du jour
        else:
            date_choice = Check.check_date("enrez la date")
            hour = Check.check_hour("entrez l'heure")
        store_id = Store.get_storeid("entrez le nom du magasin")
        card_code = Check.check_cardcode("entrez le numéro de carte")
        with machin carte_list as truc:
            la liste des cartes
        if card_code not in list_card_code:
            new_card = Check.check_yn("nouvelle carte ? ")
            if new_card == 'o':
                remove_old_card = Check.check_yn("supprimer l'ancien code ? ")
                supprimer l'ancien code
            enregistrer le nouveau code dans la liste
        enregistrer les données dans la table purchase

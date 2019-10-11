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
    def false_purchase():
        with Connection.get_cursor() as cur:
            cur.execute("""SELECT id FROM purchase WHERE purch = False;""")
            purchase_incourse_list = cur.fetchall()
        while True:
            if not purchase_incourse_list:
                print(purchase_incourse_list)
                print("la liste est vide: pas de ticket en cours d'enregistrement")
                break
            while purchase_incourse_list:
                purchase_choice = Menu.display_menu("choisissez un élément de la liste", menu=purchase_incourse_list)
                action_choice = Menu.display_menu("quelle action voulez-vous effectuer sur cet achat ?", menu="second")
                if action_choice == "continuer":
                    print("vous continuez l'enregistrement de cet achat")
                elif action_choice == "supprimer":
                    print("vouqs supprimez cdet enregistrement")
                else:
                    break

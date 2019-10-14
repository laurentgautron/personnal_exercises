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

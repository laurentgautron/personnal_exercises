from ask import Ask


class Last:

    @staticmethod
    def display_last_datas():
        with open('list_record.json', 'r') as file:
            list_record = json.load(file)
        last_purchase = list_record["purchase"]
        product_name = list_record["product"]
        last_article = list_record["article"]
        store = list_record["store"]
        nb_articles = list_record["nb_articles"]
        day = list_record["day"]
        hour = list_record["hour"]
        print("vous avez un enregistrement d'achat en cours!")
        print("le dernier produit enregistré est:", list_record["last_product"])
        print("du magasin:", list_record["store"])
        print("le %s à %s heure", (list_record['day'], list_record["hour"]))

import json


class Last:

    @staticmethod
    def display_last_datas():
        with open('list_record.json', 'r') as file:
            list_record = json.load(file)
        last_purchase = list_record["purchase"]
        last_article = list_record["article"]
        store = list_record["store"]
        nb_articles = list_record["nb_articles"]
        day = list_record["day"]
        hour = list_record["hour"]
        product = list_record['product']
        print("vous avez un enregistrement d'achat en cours!")
        if product == 'exit':
            print("vous n'avez pas enregistré de produits pour l'instant")
        else:
            print("vous avez enregistyré %s produits, le dernier produits enregistré est %s", (nb_articles, product))
        print("du magasin:", store)
        print("le %s à %s heure" % (day, hour))
        print(list_record)
        return last_purchase, last_article, store, nb_articles, day, hour

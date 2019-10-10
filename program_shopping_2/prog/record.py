from purchase import Purchase

class Record:

    @staticmethod

    def record():
        while True:
            purchase_incourse_list = Purchase.false_purchase()
            if not purchase_incourse_list:
                print(purchase_incourse_list)
                print("la liste est vide: pas de ticket en cours d'enregistrement")
            while purchase_incourse_list:

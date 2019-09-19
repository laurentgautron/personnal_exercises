from purchase import Purchase
from product import Product
from store import Store
from purchase_product import PurchaseProduct
from ask import Ask


class Record:

    @staticmethod
    def record_purchase():
        purch = 'o'
        while purch == 'o':
            last_purchase_ok = Purchase.status()
            if last_purchase_ok:
                store_id = Store.insert()
                Purchase.insert(store_id)
            last_purchase = Purchase.find_last_purchase()
            product_id = Product.record_product(last_purchase())
            PurchaseProduct.insert(last_purchase, product_id)
            purch = Ask.ask_string('voulez-vous enregistrer un autre achat? ', yn=True)

from purchase import Purchase
from product import product
from store import store
from purchase_product import Purchase_product

class Tables:

    @staticmethod
    def create():
        Purchase.create()
        Product.create()
        Purchase_product.create()
        Store.create()

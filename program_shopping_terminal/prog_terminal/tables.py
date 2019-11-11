from purchase import Purchase
from product import Product
from store import Store
from purchase_product import Purchase_product

class Tables:

    @staticmethod
    def create():
        Purchase.create()
        Product.create()
        Purchase_product.create()
        Store.create()

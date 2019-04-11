from purchase import Purchase
from store import Store
from product import Product
from purchase_store import PurchaseStore
from purchase_product import PurchaseProduct
from store_product import StoreProduct


class CreateTables:

    def __init__(self):
        Purchase.create()
        Product.create()
        Store.create()
        PurchaseProduct.create()
        PurchaseStore.create()
        StoreProduct.create()

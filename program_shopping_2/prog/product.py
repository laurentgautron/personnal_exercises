from connection import Connection

class Product:

    @staticmethod
    def create():
        with Connection.get_intance() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS product (
                        id sérial PRIMARY KEY,
                        product_name VARCHAR(100),
                        great_category VARCHAR(100),
                        category VARCHAR(100),
                        sub_category VARCHAR(100),
                        isfood BOOLEAN,
                        processed_food BOOLEAN,
                        coditionnded_weight DECIMAL(7,2));"""
                        )

from connection import Connection

class Purchase_product:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS purchase_product(
                        id SERIAL PRIMARY KEY,
                        purchase_id INT,
                        product_id INT,
                        price DECIMAL(5,2),
                        weight DECIMAL(7,2));"""
                        )

from connection import Connection

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

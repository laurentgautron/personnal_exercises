from connection import Connection

class Purchase:

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS purchase (
                        id sérial PRIMARY KEY,
                        date DATE,
                        hour TIME,
                        article_number INT(100),
                        total_price DECIMAL(5,2),
                        card_code INT(5),
                        store_id INT);"""
                        )

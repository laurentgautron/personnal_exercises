from connection import Connection

class Store:

    @staticmethod
    def create():
        with Connection.get_cursor() as cur:
            cur.execute("""CREATE TABLE IF NOT EXISTS store(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100),
                        road VARCHAR(100),
                        road_number VARCHAR(100),
                        town VARCHAR(100),
                        postcode INT,
                        bank_name VARCHAR(100));"""
                        )

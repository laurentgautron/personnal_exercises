from connection import Connection

class Store:

    @staticmethod
    def create():
        with Connection.get_instance() as cur:
            cur.execute("""CREATE TABLE IF NOT EXIISTS store(
                        id sérial PRIMARY KEY INT,
                        name VARCHAR(100),
                        road VARCHAR(100),
                        road_number VARCHAR(100),
                        town VARCHAR(100),
                        postcode INT(5),
                        bank_name VARCHAR(100));"""
                        )

import psycopg2


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname="shopping",
                user="lolo",
                password="cestmoi",
                host="localhost"
            )
            self.connection.autocommit = True
            self.cur = self.connection.cursor()
        except:
            print("cannot connect to database shopping")

    def create_tables(self):
        sql = """CREATE TABLE store (store_id serial PRIMARY KEY, name VARCHAR(100), number integer);"""
        self.cur.execute(sql)

    def insert_data(self):
        sql = """INSERT INTO store(name, number) VALUES(%s, %s);"""
        data = [("intermarche", 12), ("auchan", 45)]
        self.cur.executemany(sql, data)


if __name__ == "__main__":
    base = DatabaseConnection()
    base.create_tables()
    base.insert_data()

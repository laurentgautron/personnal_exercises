from databaseconnection import DatabaseConnection


if __name__ == "__main__":
    database = DatabaseConnection()
    DatabaseConnection.create_tables()
    database.insert_datas()

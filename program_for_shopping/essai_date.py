from connection import Connection


def base():
    with Connection.get_instance() as cur:
        cur.execute("SELECT * FROM PURCHASE;")
        datas = cur.fetchall()
        for data in datas:
            print(data)


print(base())

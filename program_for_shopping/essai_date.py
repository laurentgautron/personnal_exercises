import json
import time
import psycopg2
from datetime import datetime



def les_dates():
    sql_create = """CREATE TABLE IF NOT EXISTS essaidate (
                        id serial PRIMARY KEY,
                        ladate DATE,
                        lheure TIME);"""
    conn = psycopg2.connect(dbname="dates", user='lolo', host="localhost", password="cestmoi")
    cur = conn.cursor()
    cur.execute(sql_create)
    cur.close()
    conn.commit()
    conn.close()
    madate = input('rentrer une date: ')
    monheure = input('entrer une heure: ')
    print(type(madate))
    print(madate)
    print(type(monheure))
    print(monheure)
    madate = datetime.strptime(madate, '%d%m%Y').date()
    print(type(madate))
    print(madate)
    monheure = datetime.strptime(monheure, '%H%M%S').time()
    print(type(monheure))
    print(monheure)
    print('la date: ', madate)
    print("l'heure:'", monheure)
    conn = psycopg2.connect(dbname="dates", user='lolo', password="cestmoi", host="localhost")
    cur = conn.cursor()
    cur.execute("INSERT INTO essaidate(ladate, lheure) VALUES (%s, %s);", (madate, monheure))
    cur.close()
    conn.commit()
    conn.close()


def display():
    conn = psycopg2.connect(dbname="dates", user="lolo", password="cestmoi", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT ladate, lheure FROM essaidate WHERE id = (SELECT MAX(id) FROM essaidate);")
    result = cur.fetchone()
    conn.commit()
    print(type(result))
    print(result)
    print(result[0])
    print(type(result[0]))
    print(result[1])
    print(type(result[1]))
    heure = result[1].strftime('%H:%M:%S')
    date1 = result[0].strftime('%d-%m-%Y')
    print(type(date1))
    print(type(heure))
    print('je sors la date: ', date1)
    print('je sors \'heure: ', heure)
    cur.close()
    conn.close()
    record = {'date': date1, 'heure': heure}
    with open('date.json', 'w') as file:
        json.dump(record, file, indent=4)


les_dates()
display()

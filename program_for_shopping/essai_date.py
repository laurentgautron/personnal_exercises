import psycopg2
from datetime import datetime



def les_dates():
    sql_create = """CREATE TABLE IF NOT EXISTS essaidate (
                        id serial PRIMARY KEY,
                        ladate TIMESTAMP);"""
    conn = psycopg2.connect(dbname="dates", user='lolo', host="localhost", password="cestmoi")
    cur = conn.cursor()
    cur.execute(sql_create)
    cur.close()
    conn.commit()
    conn.close()
    madate = input('rentrer une date: ')
    monheure = input('entrer une heure: ')
    monjour = madate + ' ' + monheure
    print(monjour)
    print(type(madate))
    print(madate)
    monjour = datetime.strptime(monjour, '%d%m%Y %H%M%S')
    print(type(monjour))
    madate = monjour.date().strftime('%d-%m-%Y')
    monheure = monjour.time()
    print('la date: ', madate)
    print("l'heure:'", monheure)
    conn = psycopg2.connect(dbname="dates", user='lolo', password="cestmoi", host="localhost")
    cur = conn.cursor()
    cur.execute("INSERT INTO essaidate(ladate) VALUES (%s);", (monjour,))
    cur.close()
    conn.commit()
    conn.close()


def display():
    conn = psycopg2.connect(dbname="dates", user="lolo", password="cestmoi", host="localhost")
    cur = conn.cursor()
    cur.execute("SELECT ladate FROM essaidate WHERE id = (SELECT MAX(id) FROM essaidate);")
    result = cur.fetchone()
    conn.commit()
    print(type(result))
    print(result)
    date1 = result[0].date()
    heure = result[0].time()
    print(type(date1))
    print(type(heure))
    print('je sors la date: ', date1.strftime('%d-%m-%Y'))
    print('je sors \'heure: ', heure.strftime('%H:%M:%S'))
    cur.close()
    conn.close()


les_dates()
display()

__author__ = 'Roy'
import random
import sqlite3

conn =  sqlite3.connect('life.db')
cur = conn.cursor()

#
# create_sql = "CREATE TABLE lifetotal(ID INTEGER PRIMARY KEY AUTOINCREMENT, life INTEGER)"
# cur.execute("DROP TABLE IF EXISTS lifetotal")


create_db = "CREATE TABLE IF NOT EXISTS lifetotal(ID INTEGER PRIMARY KEY AUTOINCREMENT, life INTEGER)"


cur.execute(create_db)
# cur.execute(create_sql)

# cur.execute("INSERT INTO lifetotal (life)"
#     "VALUES ('%d')" %\
#     (20))

conn.commit()

class sql_functions:

    StartLife = 20

    sql = "SELECT life FROM lifetotal;"
    cur.execute(sql)
    results = cur.fetchall()
    g = int(results[0][0])



def gainlife():
    ew = sql_functions


    gainonelife = int(input('Enter a number: '))
    onelife = ew.g + gainonelife

    cur.execute("UPDATE lifetotal SET life = ? WHERE ID = 1", (onelife,))

    conn.commit()

gainlife()

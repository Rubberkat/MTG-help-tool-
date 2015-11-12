__author__ = 'Roy'
import random
import sqlite3

conn =  sqlite3.connect('life.db')
cur = conn.cursor()

create_sql = "CREATE TABLE lifetotal(life INTEGER)"

cur.execute("DROP TABLE IF EXISTS LIFETOTAL")
cur.execute(create_sql)


cur.execute("INSERT INTO LIFETOTAL (LIFE)"
          "VALUES ('%d')" %\
          (20))

conn.commit()

sql = "SELECT life FROM lifetotal;"
cur.execute(sql)
results = cur.fetchall()

g = int(results[0][0])


g = g + 2

print (g)

__author__ = 'Roy'
import sqlite3

conn =  sqlite3.connect('life.db')
cur = conn.cursor()

create_db = "CREATE TABLE IF NOT EXISTS lifetotal" \
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT, " \
            "life INTEGER DEFAULT 20);"

create_life = "INSERT INTO lifetotal DEFAULT VALUES"

cur.execute(create_db)
cur.execute(create_life)
conn.commit()


class sql_functions:

    sql = "SELECT life FROM lifetotal;"
    cur.execute(sql)
    results = cur.fetchall()
    g = int(results[0][0])

    def __init__(self, x):
        self.starting_life = x

    def gainlife(self):
        ew = sql_functions
        gainonelife = int(input('Enter a number: '))
        onelife = ew.g + gainonelife
        cur.execute("UPDATE lifetotal "
                    "SET life = ? WHERE ID = 1", (onelife,))
        conn.commit()


    def loseLife(self):
        lose = sql_functions
        lose_life = int(input ('Enter a number: '))
        lost_total = lose.g - lose_life
        cur.execute("UPDATE lifetotal "
                    "SET life = ? WHERE ID = 1", (lost_total,))
        conn.commit()


    def resetLifeTotal(self):
        reset = sql_functions(20)
        cur.execute("UPDATE lifetotal SET life = ? WHERE ID = 1", (reset.starting_life,))
        conn.commit()







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


class starting_life_list:

    sql = "SELECT life FROM lifetotal;"
    cur.execute(sql)
    results = cur.fetchall()
    life_list = int(results[0][0])

    def __init__(self, x):
        self.starting_life = x





def gainLife():
    gain = starting_life_list
    gain_life = int(input('Enter a number: '))
    gain_total = gain.life_list + gain_life
    
    cur.execute(
                "UPDATE lifetotal "
                "SET life = ? WHERE ID = 1",
                (gain_total,)
    )
    conn.commit()


def loseLife():
    lose = starting_life_list
    lose_life = int(input ('Enter a number: '))
    lost_total = lose.life_list - lose_life
    
    cur.execute(
                "UPDATE lifetotal "
                "SET life = ? WHERE ID = 1",
                (lost_total,)
    )
    conn.commit()


def resetLifeTotal():
    reset = starting_life_list(20)
    
    cur.execute(
                "UPDATE lifetotal "
                "SET life = ? WHERE ID = 1",
                (reset.starting_life,)
    )
    conn.commit()





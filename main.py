__author__ = 'Roy'
from life_functions import *

cur.execute ("CREATE TABLE IF NOT EXISTS lifetotal"
            "(ID INTEGER PRIMARY KEY AUTOINCREMENT, life INTEGER DEFAULT 20);")

select = "SELECT ID FROM lifetotal WHERE ID = 1"
cur.execute(select)
results = cur.fetchone()
if not results:
    cur.execute ("INSERT INTO lifetotal DEFAULT VALUES")


conn.commit()


cur.execute("SELECT life FROM lifetotal;")
results = cur.fetchall()
life_list = results[0][0]


player1 = player()
def playerOne():
    player1.starting_life = 20
    player1.ID = 1
    player1.gainLife()

playerOne()

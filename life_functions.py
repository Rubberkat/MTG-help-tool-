__author__ = 'Roy'
from main import *
import sqlite3


conn =  sqlite3.connect('life.db')
cur = conn.cursor()


class player:

    ID = 0
    starting_life = 20


    def gainLife(self):

        try:
            gain_life = int(input('Enter a number: '))
            gain_total = life_list + gain_life
            cur.execute("UPDATE lifetotal SET life = ? WHERE ID = ?",
                        (gain_total, self.ID,))
            conn.commit()
        except:
            print ('Error, please enter a number.')


    def loseLife(self):

        try:
            lose_life = int(input ('Enter a number: '))
            lost_total = life_list - lose_life
            cur.execute("UPDATE lifetotal SET life = ? WHERE ID = ?",
                        (lost_total, self.ID,))
            conn.commit()
        except:
            print ('Error, please enter a number.')


    def resetLifeTotal(self):
        print ('Life has been reset to:', self.starting_life)
        cur.execute("UPDATE lifetotal SET life = ? WHERE ID = ?",
                    (self.starting_life, self.ID,))
        conn.commit()

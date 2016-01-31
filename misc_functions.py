__author__ = 'Roy'

import random
import time

def flipcoin():

    coin = ['Heads', 'Tails']
    coinflip = random.choice(coin)
    print ('Flipping a coin...')
    time.sleep(0.5)
    print (coinflip)


class dices:

    def randomizer(self, x, y):
        print ('Rolling the dice...')
        time.sleep(0.5)
        print ('The number is:', random.randrange(x, y))


dice = dices
dice.randomizer(dices, 1, 20)




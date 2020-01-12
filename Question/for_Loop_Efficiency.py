import time
from itertools import product

def simulation1(SUITS, RANKS):
    #progressing start
    start_time = time.time()


    deck = [(s, r) for r in RANKS for s in SUITS]


    #progressing end
    end_time = time.time()
    return end_time - start_time

def simulation2(SUITS, RANKS):
    # progressing start
    start_time = time.time()

    deck = list(product(RANKS, SUITS))

    # progressing end
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":

    SUITS = "♠ ♡ ♢ ♣".split() * 1000
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split() * 1000
    print(simulation1(SUITS, RANKS))
    print(simulation1(SUITS, RANKS))

    #result
    #simulation1 = 6.825436353683472
    #simulation2 = 5.459356069564819

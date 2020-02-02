import time
from itertools import product
from typing import Tuple, Sequence


def simulation1(lhs: Sequence[str], rhs: Sequence[str]) -> Tuple[list, float]:
    # progressing start
    start_time = time.time()
    deck = [(l, r) for l in lhs for r in rhs]

    # progressing end
    end_time = time.time()
    return deck, end_time - start_time


def simulation2(lhs: Sequence[str], rhs: Sequence[str]) -> Tuple[list, float]:
    # progressing start
    start_time = time.time()

    deck = list(product(lhs, rhs))

    # progressing end
    end_time = time.time()
    return deck, end_time - start_time


if __name__ == "__main__":
    suits = "♠ ♡ ♢ ♣".split() * 100
    ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split() * 100

    for _ in range(10):
        deck1, time1 = simulation1(suits, ranks)
        deck2, time2 = simulation1(suits, ranks)

        assert deck1 == deck2
        print(time1, time2)
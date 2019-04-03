#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    a, b, c = 0, 0, 0
    for x in arr:
        if x > 0:
            a += 1
        elif x < 0:
            b += 1
        elif x == 0:
            c += 1
    v = len(arr)
    a, b, c = round(a / v, 6), round(b / v, 6), round(c / v, 6)
    a, b, c = float("%0.6f" % a), float("%0.6f" % b), float("%0.6f" % c)
    print(f"{a}\n{b}\n{c}")


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

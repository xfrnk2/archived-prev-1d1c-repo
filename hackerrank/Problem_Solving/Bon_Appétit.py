#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    v = 0
    for i, j in enumerate(bill):
        if i == k:
            continue
        else:
            v += j

    v = int(v / 2)

    if b == v:
        print("Bon Appetit")
    else:
        print(b - v)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

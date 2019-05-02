#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    size = len(scores)
    high = low = -1
    hv, lv = -sys.maxsize, sys.maxsize

    if size == 1:
        return 0, 0

    for i, j in enumerate(scores):

            if hv < j:
                hv = j
                high += 1
            if j < lv:
                lv = j
                low += 1

    return high, low

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

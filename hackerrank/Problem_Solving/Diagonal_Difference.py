#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    v = [x for x in range(0, len(arr))]
    v2 = list(reversed(v))

    a, b = 0, 0
    for x, y in zip(v, v2):
        a += arr[x][x]
        b += arr[x][y]

    return abs(a-b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

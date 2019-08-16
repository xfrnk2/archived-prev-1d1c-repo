#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    i = 0
    i2 = l = len(arr)

    a, b = 0, 0

    for _ in range(l):
        a += arr[i][i]
        b += arr[i][i2 - 1]
        i += 1
        i2 -= 1

    return abs(a - b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

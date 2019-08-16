#!/bin/python3

import os
import sys


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    v = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            v += 1
    return v


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

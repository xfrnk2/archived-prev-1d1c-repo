#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):

    if p == 1 or n == p:
        return 0
    if p <= n - p :
        return p//2

    d = n-p

    if d >= 2:
        if n % 2 == 0:
            if p == n-1:
                return 1
            if p % 2 == 0:
                return d//2
            else:
                return d//2 + 1
        return d//2


    if n % 2 == 0:
        return 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

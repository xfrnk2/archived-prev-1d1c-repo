#!/bin/python3

import os
import sys
import itertools


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    values = [-1]
    max_value = 0
    for x, y in itertools.product(keyboards, drives):
            z = x + y
            if max_value < z <= b:
                values.append(z)
                max_value = z
    return max(values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

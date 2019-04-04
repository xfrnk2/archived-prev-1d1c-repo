#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    H = 0
    V = 0
    for n in s:
        if n == 'U':
            H += 1
            if H == 0:
                V += 1
        else:
            H -= 1
    return V


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

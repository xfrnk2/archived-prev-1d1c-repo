#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):

    if len(a) <= 1:
        return len(a)

    a.sort()
    numbers = set(a)
    result = 0

    for num in numbers:
        if num < 2:
            continue
        count = 0
        for y in a:
            if y == num or num - 1 == y:
                count += 1
        if result < count:
            result = count

    return (result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

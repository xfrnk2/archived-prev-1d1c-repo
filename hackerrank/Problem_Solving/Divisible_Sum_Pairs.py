#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations


# Complete the divisibleSumPairs function below.

def divisibleSumPairs(n, k, ar):
    count = 0

    if n < 2:
        return 0

    elif k == 1:
        v = list(permutations(ar, 2))
        return len(v)

    elif n == 2:
        if sum(ar) % k == 0:
            return 1

    for x in range(n):
        for y in range(x + 1, n):
            if (ar[x] + ar[y]) % k == 0:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

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

    if k == 1:
        return len(list(permutations(ar, 2)))

    if n == 2 and sum(ar) % k == 0:
        return 1

    for x in range(n):
        for y in range(x + 1, n):
            if (ar[x] + ar[y]) % k == 0:
                count += 1

    return count


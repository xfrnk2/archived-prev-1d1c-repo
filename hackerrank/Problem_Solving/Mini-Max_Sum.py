#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    mn = mx = arr[0]
    all = 0

    for n in arr:
        if mx < n:
            mx = n
        if mn > n:
            mn = n
        all += n

    mn, mx = all - mx, all - mn
    print(mn, mx)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    if len(arr) < 5:
        print("Wrong input")
        exit()

    mn = mx = arr[0]
    all = 0

    for n in arr:
        if n < 1:
            print("Wrong element value")
            exit()

        if mx < n:
            mx = n
        if mn > n:
            mn = n
        all += n

    mn, mx = all - mx, all - mn
    print(mn, mx)


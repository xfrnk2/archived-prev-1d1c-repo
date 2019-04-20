#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    size = len(arr)

    if size == 1:
        return arr[0]

    box = {}
    temp = temp_num = 0

    for x in arr:
        if not x in box:
            box[x] = 0
        box[x] += 1

    for num, val in box.items():
        if val > temp:
            temp = val
            temp_num = num
        if val == temp:
            if num < temp_num:
                temp_num = num
                temp = val

    return temp_num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

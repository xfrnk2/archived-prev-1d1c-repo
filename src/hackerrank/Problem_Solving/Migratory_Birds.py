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
        if x not in box:
            box[x] = 0
        box[x] += 1

    for num, val in box.items():
        if val > temp:
            temp = val
            temp_num = num
        elif val == temp:
            if num < temp_num:
                temp_num = num
                temp = val

    return temp_num


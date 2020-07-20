#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zero_value = 0, 0, 0
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        elif x == 0:
            zero_value += 1
    v = len(arr)
    positive, negative, zero_value =\
        round(positive / v, 6), round(negative / v, 6), round(zero_value / v, 6)
    positive, negative, zero_value =\
        float("%0.6f" % positive), float("%0.6f" % negative), float("%0.6f" % zero_value)
    print(f"{positive}\n{negative}\n{zero_value}")


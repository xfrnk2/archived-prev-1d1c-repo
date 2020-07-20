#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    size = len(scores)
    high = low = -1
    hv, lv = -sys.maxsize, sys.maxsize

    if size == 1:
        return 0, 0

    for x in scores:

            if hv < x:
                hv = x
                high += 1
            if x < lv:
                lv = x
                low += 1

    return high, low

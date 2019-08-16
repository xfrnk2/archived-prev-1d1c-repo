#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    c = 0
    for x in range(i, j + 1):
        v = abs(x - int(str(x)[::-1]))
        if v % k == 0:
            c += 1
    return c
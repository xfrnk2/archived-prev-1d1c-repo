#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ap = 0
    bp = 0
    for x, y in zip(a, b):
        if x == y:
            continue
        if x > y:
            ap += 1
        else:
            bp += 1
    return ap, bp

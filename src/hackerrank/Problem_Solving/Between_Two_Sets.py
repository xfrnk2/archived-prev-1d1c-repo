#!/bin/python3

import os
import sys


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    v = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            v += 1
    return v

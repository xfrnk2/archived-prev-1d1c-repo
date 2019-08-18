#!/bin/python3

import os
import sys
import itertools


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    values = [-1]
    max_value = 0
    for x, y in itertools.product(keyboards, drives):
            z = x + y
            if max_value < z <= b:
                values.append(z)
                max_value = z
    return max(values)


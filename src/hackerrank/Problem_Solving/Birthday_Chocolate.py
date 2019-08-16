#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    n = len(s)
    for x in range(n - m + 1):
        if sum(s[x:x + m]) == d:
            result += 1

    return result


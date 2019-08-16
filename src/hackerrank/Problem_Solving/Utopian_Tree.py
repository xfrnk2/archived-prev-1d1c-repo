#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n):
    if 0 <= n < 3:
        return n + 1
    count = 3
    for x in range(n - 2):
        if x % 2 == 0:
            count *= 2
            continue
        count += 1
    return count


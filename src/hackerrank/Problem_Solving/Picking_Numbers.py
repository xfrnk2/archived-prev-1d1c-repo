#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    if len(a) <= 1:
        return len(a)

    numbers = set(a)
    result = 0

    for num in numbers:
        if num < 2:
            continue
        count = 0

        for _ in filter(lambda x: x == num or x == num - 1, a):
            count += 1

        if result < count:
            result = count

    return (result)


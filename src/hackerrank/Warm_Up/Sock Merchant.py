#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    counts = {}
    for x in ar:
        if not x in counts:
            counts[x] = 0
        counts[x] += 1

    result = 0
    for v in counts.values():
        result += v // 2

    return result


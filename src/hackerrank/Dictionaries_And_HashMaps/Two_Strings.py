#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    if s1.intersection(s2):
        return("YES")
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = set(input())

        s2 = set(input())

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

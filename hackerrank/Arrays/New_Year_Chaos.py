import copy

# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
import copy


def minimumBribes(q):
    count = 0
    group = {}
    l = len(q)
    for x in range(l):
        group[q[x]] = 0

    for i in range(l, 0, -1):
        for j in range(1, i):

            if q[j] < q[j - 1]:
                q[j], q[j - 1] = q[j - 1], q[j]
                if not q[j] in group:
                    group[q[j]] = 0
                count += 1
                group[q[j]] += 1
                if group[q[j]] > 2:
                    return "Too chaotic"


    return count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))

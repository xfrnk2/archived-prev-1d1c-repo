# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    minus_count = 0
    flag = False

    for x in c:

        i = c.index(x)

        if x == 0:
            if i < len(c) - 2:
                if c[i + 1] == c[i + 2]:
                    flag = True

            count += 1
        if flag:
            flag = False
            minus_count += 1

    return count - minus_count


value = 6
q = 0, 0, 0,  1, 0, 0
print(jumpingOnClouds(q))
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     c = list(map(int, input().rstrip().split()))
#
#     result = jumpingOnClouds(c)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

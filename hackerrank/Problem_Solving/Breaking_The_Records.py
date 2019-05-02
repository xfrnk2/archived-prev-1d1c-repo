#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    size = len(scores)
    high = low = hv = lv = 0

    if size == 1:
        return 0, 0

    for i, j in enumerate(scores):
        if i == 0:
            hv = lv = j
        else:
            if hv < j:
                hv = j
                high += 1
            if j < lv:
                lv = j
                low += 1
<<<<<<< HEAD
<<<<<<< HEAD

    return high, low

<<<<<<< HEAD
=======
 
=======

>>>>>>> Pytest 학습, 테스트 가능한 구조로 만들기
    return high, low


>>>>>>> Breaking_The_Records (성공)
=======
>>>>>>> 폴더명을 tdd -> tests로 변경, Travi-ci와 Coverall 뱃지 추가
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

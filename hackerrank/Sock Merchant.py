# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
#
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
#
# Function Description
#
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
#
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
#
# Constraints
#
#  where
# Output Format
#
# Return the total number of matching pairs of socks that John can sell.
#
# Sample Input
#
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
#
# 3

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    # 첫번째 풀이 
    # all_count = 0
    # array = list(set(ar))
    # for x in array:
    #     if ar.count(x) >= 2:
    #         all_count += ar.count(x) // 2
    #
    # return all_count


    # 두번째 풀이 -  두번째 풀이도 흐름은 똑같은데..
    setted_ar = list(set(ar))
    a = list(map(lambda x: ar.count(setted_ar[x]), range(len(setted_ar))))
    b = list(map(lambda x: x // 2, a))
    return sum(int(i) for i in b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

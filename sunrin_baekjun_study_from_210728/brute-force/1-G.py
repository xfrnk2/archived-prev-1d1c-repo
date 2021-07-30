# https://www.acmicpc.net/problem/14888
from itertools import permutations
import sys

n = int(input())
op = ['+', '-', '*', '//']

num_arr = list(input().split())
op_counts = list(map(int, input().split()))
operators = []

for x, y in zip(op ,op_counts):
    for _ in range(y):
        operators.append(x)



sqs = set(permutations(operators))

max_value = - sys.maxsize - 1
min_value = sys.maxsize

for opr in sqs:
    result = int(num_arr[0])
    for i in range(len(opr)):
        if opr[i] == op[3]:
            temp = result
            result = eval(str(abs(result)) + op[3] + num_arr[i + 1])
            if temp < 0:
                result *= -1
        else:
            result = eval(str(result) + opr[i] + num_arr[i+1])

    max_value = max(max_value, result)
    min_value = min(min_value, result)
print(max_value)
print(min_value)

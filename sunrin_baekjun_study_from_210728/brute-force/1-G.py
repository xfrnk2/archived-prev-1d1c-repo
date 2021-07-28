# https://www.acmicpc.net/problem/14888
from itertools import permutations
n = int(input())

num_arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

op = ['+', '-', '*', '%']
n_a = list(permutations(op))
cnt = 0
idx = 0
max_v = 1e9
min_v = 0
for _ in range(len(n_a)):
    result = num_arr[0] + op[idx] + num_arr[1]
    for i in range(2, len(num_arr)):




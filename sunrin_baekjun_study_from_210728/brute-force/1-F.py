# https://www.acmicpc.net/problem/10819
from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
max_sum = 0

for item in list(permutations(arr)):
    temp = 0
    for i in range(n-1):
        temp += abs(item[i] - item[i+1])
    max_sum = max(temp, max_sum)

print(max_sum)
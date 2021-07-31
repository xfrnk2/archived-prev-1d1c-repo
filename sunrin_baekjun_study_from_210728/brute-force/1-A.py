# https://www.acmicpc.net/problem/1182
from itertools import combinations

n, s = list(map(int, input().split()))
numbers = list(map(int, input().split()))
c = 0

for i in range(1, n+1):
    for j in list(map(sum, combinations(numbers, i))):
        if j == s:
            c += 1
print(c)







'''
input
5 0
output
-7 -3 -2 5 8
'''
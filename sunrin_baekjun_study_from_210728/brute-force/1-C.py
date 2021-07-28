# https://www.acmicpc.net/problem/10974
from itertools import permutations
n = int(input())

result = ''
for element in list(permutations(range(1, n+1))):
    for item in element:
        print(item, end=' ')
    print()
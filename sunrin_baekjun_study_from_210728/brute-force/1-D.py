# https://www.acmicpc.net/problem/2309
from itertools import permutations
n = [int(input()) for _ in range(9)]
items = list(permutations(n, 7))
result = items[0]
for item in items:
    value = sum(item)
    if value == 100:
        result = item
    else:
        continue

for i in sorted(result):
    print(i)



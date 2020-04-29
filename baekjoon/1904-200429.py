# 링크 : https://www.acmicpc.net/problem/1904
# 시간 초과가 나왔다. 야매로 풀면 안되나 보다.
from itertools import product
n = int(input())
a = [1, 2]

result = 0
if n <= 2 :
    print(n%15746)
else:
    for x in range(2, n+1):
        b = [v for v in product(a, repeat=x) if sum(v) == n]
        result += len(b)
    print(result%15746)

'''
211 0011
22 0000
1111 1111
112 0011
121 1001
'''

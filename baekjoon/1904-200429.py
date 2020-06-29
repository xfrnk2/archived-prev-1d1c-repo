# 링크 : https://www.acmicpc.net/problem/1904
# ↓시간 초과가 나왔다. 야매로 풀면 안되나 보다.
# from itertools import product
# n = int(input())
# a = [1, 2]
#
# result = 0
# if n <= 2 :
#     print(n%15746)
# else:
#     for x in range(2, n+1):
#         b = [v for v in product(a, repeat=x) if sum(v) == n]
#         result += len(b)
#     print(result%15746)

'''
N이 1일때~의 결괏값을 살펴보면
N= 1 -> 1
N= 2 -> 00 11
N= 3 -> 001 100 111
N= 4 -> 0011 1100 1001 1111 0000
N= 5 -> 00001 10000 00100 11100 00111 11001 10011 11111

=> 1, 2, 3, 5, 8 -> 피보나치 수열의 문제였다.

'''

n = int(input())
lhs, rhs = 1, 1

if 2 <= n:
    for _ in range(n-1):
        lhs, rhs = rhs, lhs
        rhs = (lhs+ rhs)%15746
    print(rhs)
else:
    print(n)

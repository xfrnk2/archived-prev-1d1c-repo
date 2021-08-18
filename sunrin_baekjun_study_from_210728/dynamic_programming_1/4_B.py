# https://www.acmicpc.net/problem/11441
# input을 쓰니 시간 초과가 뜨길래, sys.stdin.readline을 사용했더니 통과했다.
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# dp = [0] * N
# dp[0] = A[0]
#
# for i in range(1, N):
#     dp[i] = dp[i-1] + A[i]
# dp.insert(0, 0)
#
# for _ in range(M):
#     lhs, rhs = list(map(int, input().split()))
#     print(dp[rhs] - dp[lhs-1])



#약간의 리팩토링을 거친 코드
import sys


N = int(input())
A = [0] + list(map(int, sys.stdin.readline().split()))
M = int(input())

for i in range(1, N+1):
    A[i] += A[i-1]

for _ in range(M):
    lhs, rhs = map(int, sys.stdin.readline().split())
    print(A[rhs] - A[lhs-1])

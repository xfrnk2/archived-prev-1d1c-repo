# https://www.acmicpc.net/problem/11066
# 풀이를 보고 이해한 곳(설명이 아주 좋았다.) : https://data-make.tistory.com/402
import sys
def func():

    K = int(sys.stdin.readline())
    NUM = list(map(int, sys.stdin.readline().split()))

    dp = [[0] * (K+1) for _ in range(K+1)]
    acc = [0 for _ in range(K+1)]
    for i in range(1, K+1):
        acc[i] = acc[i-1] + NUM[i-1]

    for k in range(1, K):
        for i in range(1, K - k + 1):
            lhs, rhs = i, i+k
            dp[lhs][rhs] = (acc[rhs] - acc[lhs-1]) + min([dp[lhs][lhs+j] + dp[lhs+j+1][rhs] for j in range(k)])

    print(dp[1][K])
for _ in range(int(sys.stdin.readline())):
    func()




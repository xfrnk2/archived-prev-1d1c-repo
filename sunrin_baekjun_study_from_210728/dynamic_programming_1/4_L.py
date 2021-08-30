# https://www.acmicpc.net/problem/12920
# 첫번째 풀이, 메모리 초과가 나온다.
# import sys
# N, M = map(int, input().split())
# item = [(0, 0)]
#
# for _ in range(N):
#     i, j, k = map(int, sys.stdin.readline().split())
#     for _ in range(k):
#         item.append((i, j))
#
# dp = [[0] * (M+1) for _ in range(len(item))]
#
# for i in range(1, len(item)):
#     for j in range(1, M+1):
#
#         if j >= item[i][0]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
#         else:
#             dp[i][j] = dp[i-1][j]
#
# print(dp[len(item)-1][M])






# 두번째 풀이, 아직 이해가 잘 되지 않는다. 퍼왔고, 50%정도 이해
# https://sangminlog.tistory.com/entry/boj-12920-1
N, M = map(int, input().split())

dp = [0 for _ in range(M+1)]
weight, satisfaction = [], []
for _ in range(N):
    V, C, K = map(int, input().split())

    idx = 1
    while K > 0:
        tmp = min(idx, K)

        weight.append(V * tmp)
        satisfaction.append(C * tmp)

        idx *= 2
        K -= tmp

for i in range(len(weight)):
    for j in range(M, 0, -1):
        if j >= weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]] + satisfaction[i])

print(dp[M])

# # https://www.acmicpc.net/problem/12865
# N, K = map(int, input().split())
# d = dict()
# for i in range(N):
#     d[i] = tuple(map(int, input().split()))
# '''
# input
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 0 1 2 3 4 5 6 7
# 6 0 0 0 0 0 13 13
# 4 0 0 0 8 8 13 13
# 3 0 0 6 8 8 13 14
# 5 0 0 6 8 12 13 14
# '''
# dp = [[n for n in range(K)]] + [[0 for _ in range(K)] for _ in range(N)]
#
# for i in range(1, N+1):
#     for j in range(K):
#         if dp[i][j] <= d[i-1]
#

# 퍼온 코드. 이해는 했는데 어떻게 짜야 하나 난감했는데, 보고 이해도가 깊어진 것 같다.
# import sys
#
# (N, K) = map(int, sys.stdin.readline().split())
# item = [[0, 0]]
# for i in range(1, N + 1):
#     item.append(list(map(int, sys.stdin.readline().split())))
# dp = [[0] * (K + 1) for _ in range(N + 1)]    # (N+1) x (K+1) matrix
#
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         if j >= item[i][0]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-item[i][0]] + item[i][1])
#         else:
#             dp[i][j] = dp[i-1][j]
#
# print(dp[N][K])


# 이제 머릿속에 있는 로직을 가지고 직접 짜보자.

import sys
N, K = map(int, sys.stdin.readline().split())
items = [(0, 0)]
for _ in range(N):
    items.append(tuple(map(int, sys.stdin.readline().split())))



dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if items[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], items[i][1] + dp[i-1][j-items[i][0]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])




'''
input
4 7
6 13
4 8
3 6
5 12
'''
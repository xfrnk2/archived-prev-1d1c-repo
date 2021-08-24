# https://www.acmicpc.net/problem/9095
# 첫번째 풀이
n = int(input())
dp = [0, 1, 2, 4] + [0] * 8

prev_update = 4
for _ in range(n):
    s = int(input())
    if s <= 3:
        print(dp[s])
    else:
        for i in range(prev_update, s+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        prev_update = s
        print(dp[s])


'''
3
4
7
10
'''
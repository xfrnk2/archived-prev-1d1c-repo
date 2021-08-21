# https://www.acmicpc.net/problem/11726
n = int(input())
dp = [0, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[-1]%10007)
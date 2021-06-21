









x = int(input())
dp = [0]*(x+1)



for i in range(3, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i]//2)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i]//3)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i]//5)
    print(i, dp[i])
print(dp[x])
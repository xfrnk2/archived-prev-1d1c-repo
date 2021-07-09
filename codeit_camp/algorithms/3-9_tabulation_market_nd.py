def max_profit(price_list, count):
    dp = [0] * (count + 1)

    for i in range(1, count + 1):

        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], dp[i - j] + dp[j])
        if i < len(price_list):
            dp[i] = max(dp[i], price_list[i])

    return dp[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

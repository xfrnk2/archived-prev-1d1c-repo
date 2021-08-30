# 모르겠다. 고민을 하다 안되겠다 싶어서 검색후 풀이를 보았다.
# 아직 이해가 잘 안된다. 시간을 너무 뻇길 수 없다.
# https://www.acmicpc.net/problem/19645
import sys

input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
total = sum(values)

dp = [[0] * (50 * n + 1) for _ in range(50 * n + 1)]  # 조합 체크

dp[0][0] = 1
for k in range(n):
   for i in range(total, -1, -1):
      for j in range(total, -1, -1):
         if i - values[k] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - values[k]][j])
         if j - values[k] >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j - values[k]])

result = 0
for i in range(total + 1):
   for j in range(i + 1):
      if dp[i][j] and j >= total - i - j:
         result = max(result, total - i - j)

print(result)
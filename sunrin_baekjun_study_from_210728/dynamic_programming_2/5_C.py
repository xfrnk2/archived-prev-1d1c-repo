# https://www.acmicpc.net/problem/11053
# 생각했던대로 코드가 안짜여서 풀이를 보고 금새 이해가 되었다. 나중에 다시 풀어볼 것.
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))



'''
4 9 1 5 3 4


8
4 2 8 9 1 5 3 4

0 1 2 3 4 5 6 7 8


 



'''
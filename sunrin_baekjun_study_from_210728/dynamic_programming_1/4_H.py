# https://www.acmicpc.net/problem/10422
# 처음으로 세운 점화식이 틀렸다. 카탈린 수열 키워드로 검색하면 힌트가 있을 것이라 그랬다.
# 찾아보고 대충 보고 직접 점화식을 찾는 시도를 거치고 있다.

# 쓰다  만 것. 실패 코드
# dp = [0] * 5001
# dp[2] = 1
#
# for i in range(4, 5001, 2):
#     dp[i] = dp[i-2] * 2
#
# for _ in range(int(input())):
#     n = int(input())
#     if n % 2 == 1:
#         print(0)
#     else:
#         print(dp[n]%1000000007)


'''
0 1 
2 1
4 2
6 5
8 14
10 42
'''

# https://week-year.tistory.com/172
# 검색을 통해 찾은 코드를 이해 후 작성. 그런데 카탈린 수는 아직 이해가 잘 안된다.
dp = [0] * 5001
dp[0] = 1

# for n in range(2, 5001, 2):
#     for i in range(2, n + 1, 2):
#         dp[n] += dp[i - 2] * dp[n - i]
#
#     dp[n] %= 1000000007
#
# for _ in range(int(input())):
#     print(dp[int(input())])


# 두 번째 코드. 검색을 통해서 카탈린 수 공식을 넣었다.
# TODO-카탈린 수를 다루는 문제를 여러개 더 풀어보고 싶다. 풀어보자.
import sys,math


def catalan(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))


T = int(sys.stdin.readline().strip())
for _ in range(T):
    L = int(sys.stdin.readline().strip())
    if L % 2 == 1:
        print(0)
    else:
        print(catalan(L // 2) % 1000000007)
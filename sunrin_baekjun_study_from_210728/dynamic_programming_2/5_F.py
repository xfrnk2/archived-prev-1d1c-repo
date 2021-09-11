# https://www.acmicpc.net/problem/9251
# 처음에 아이디어는 생각이 났는데 엄한데서 잠깐 헤맸다.
# 그래서 견본이 되는 다른 사람 풀이를 대강 훑어보니 할 수 있을 것 같았고,
# 50%정도의 도움을 받아 아래와 같이 코딩했다.
lhs = input()
rhs = input()
dp = [[ 0 for _ in range(len(rhs)+1)] for _ in range(len(lhs)+1)]
# dp[i][j]는 lhs의 i에서 rhs의 j까지의 총 길이
for i in range(1, len(lhs)+1):
    for j in range(1, len(rhs)+1):
        if lhs[i-1] == rhs[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])


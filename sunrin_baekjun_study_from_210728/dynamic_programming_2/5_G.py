# https://www.acmicpc.net/problem/15483


# 첫번째 풀이, 틀린 풀이

# lhs, rhs = input(), input()
# max_length = max(len(lhs), len(rhs))
# count = 0

# for i in range(1, max_length + 1):
#     flag = True
#     for j in range(i):
#         if lhs[j:i] in rhs[:i+1]:
#             l = len(lhs[j:i])
#             if rhs.index(lhs[j:i]) + l <= i:
#                flag = True
#             else:
#                 flag = False
#             break
#     if flag:
#         count += 1
# print(count)
        # 더하기

# 두번째 풀이, 인터넷 검색으로 풀이를 눈으로 한번 스캔하고, 이후 하루 뒤에 방법만을 되살려 직접 코딩했다.

lhs, rhs = input(), input()


dp = [[0 for _ in range(len(rhs)+1)] for _ in range(len(lhs)+1)]
for i in range(1, len(lhs)+1):
    dp[i][0] = i
for j in range(1, len(rhs)+1):
    dp[0][j] = j


for i in range(1, len(lhs) + 1):
    for j in range(1, len(rhs) + 1):

        if lhs[i-1] == rhs[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[-1][-1])



#print(lhs[j:i])
# 0 0
# 1 0
# 1 1
# 2 0
# 2 1
# 2 2




# https://www.acmicpc.net/problem/1182

# 1차 풀이, combinations 사용
# from itertools import combinations
# 
# n, s = list(map(int, input().split()))
# numbers = list(map(int, input().split()))
# c = 0
# 
# for i in range(1, n+1):
#     for j in list(map(sum, combinations(numbers, i))):
#         if j == s:
#             c += 1
# print(c)

# ----------------------- 더 즣은 방법?
# 2차 풀이, 재귀 사용..
def dfs(idx, cur):
    global c
    if n <= idx:
        return
    cur += numbers[idx]
    if cur == s:
        c += 1
    idx += 1
    dfs(idx, cur)
    dfs(idx, cur-numbers[idx-1])

dfs(0, 0)
print(c)
# 처음에는 dfs(idx, cur), 그리고 dfs(idx+1, cur)과 같은 형태로 구현해서 틀렸다. 어디서 틀린지 몰라 만지다가 해결됬다.




'''
input
5 0
output
-7 -3 -2 5 8
'''
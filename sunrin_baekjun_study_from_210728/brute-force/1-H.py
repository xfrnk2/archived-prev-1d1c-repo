# https://www.acmicpc.net/problem/1342
# from itertools import permutations
# S = input()
# p = set(permutations(S))
# ans = 0
#
# for m in p:
#
#     flag = True
#     for i in range(1, len(m)):
#         if m[i-1] == m[i]:
#             flag = False
#             break
#         else:
#             continue
#
#     if flag:
#         ans += 1
# print(ans)
#

# 인터넷 검색으로 알아본 다른사람의 코드
import sys
input = sys.stdin.readline

def dfs(pre_word, picked):

    if picked == len(S):
        return 1
    answer = 0
    for key in counter.keys():
        if pre_word == key:
            continue
        if counter[key] == 0:
            continue
        counter[key] -= 1
        answer += dfs(key, picked+1)
        counter[key] += 1
    return answer

S = list(input().strip())
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

answer = dfs('', 0)
print(answer)
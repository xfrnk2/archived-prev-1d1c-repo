# https://www.acmicpc.net/problem/2217
# 첫번째 풀이, 시간초과
# N = int(input())
# rope = []
# for _ in range(N):
#     rope.append(int(input()))
#
#
# def func(N, rope):
#     ans = max(rope)
#     for i in range(ans+1, 10000):
#         weight = i / N
#         for j in rope:
#             if j < weight:
#                 return ans
#         ans = i
# print(func(N, rope))
#

# 두번째 풀이, 틀림

# N = int(input())
# rope = []
# for _ in range(N):
#     rope.append(int(input()))
# m = max(rope)
# rope_ = [i * N for i in rope]
# n = min(rope_)
# print(max(m, n))

'''
3
30
20
10

40
'''
# 세번째 풀이. 성공
N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
c = 0
for i in range(len(rope)):
    c = max(c, rope[i] * (i+1))

print(c) #






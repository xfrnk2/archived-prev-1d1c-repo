# https://www.acmicpc.net/problem/2812
# 첫 번째 풀이, 실패한다.
# N, K = map(int, input().split())
# num = input()
#
# count = 0
# idx_stack = []
# i_count = 1
# while count < K:
#
#     for i, j in enumerate(num):
#         if K <= len(idx_stack):
#             break
#         if i_count == int(j):
#             count += 1
#             idx_stack.append(i)
#     i_count += 1
# idx_stack.sort()
# idx_stack.append(0)
# print(idx_stack)
# output = ''
# for i in range(N):
#     if idx_stack:
#         if i == idx_stack[0]:
#             idx_stack.pop(0)
#         else:
#             output += num[i]
#
# print(output)

# 검색을 통해 그대로 복붙한 남의 코드, 보고 이해함.
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().strip()))
#
# result = []
# delNum = K
#
# for i in range(N):
#     while delNum > 0 and result:
#         if result[len(result) - 1] < nums[i]:
#             result.pop()
#             delNum -= 1
#         else:
#             break
#     result.append(nums[i])
#
# for i in range(N - K):
#     print(result[i], end="")


# 검색해서 나온 코드를 보지 않고, 이해했던 느낌을 살려서 짜 보는 코드.

N, K = map(int, input().split())
num = list(map(int, input()))
stack = []
t = K
for i in range(N):


    while stack and 0 < K:
        if stack[-1] < num[i]:
            stack.pop()
            K -= 1
        else:
            break

    stack.append(num[i])
for i in range(N-t):
    print(stack[i], end='')

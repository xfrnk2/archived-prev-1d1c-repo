# https://www.acmicpc.net/problem/1725
# 인터넷 검색으로 나온 풀이를 보고 이해

# import sys
#
# input = sys.stdin.readline
# n = int(input())
# graph = []
# result = 0
# cursor = 0
# a = 0
# for _ in range(n):
#     graph.append(int(input()))
# graph.append(0)
# stack = [(0, graph[0])]
# for i in range(1, n + 1):
#     cursor = i
#     while stack and stack[-1][1] > graph[i]:
#         cursor, temp = stack.pop()
#         result = max(result, temp * (i - cursor))
#     stack.append((cursor, graph[i]))
#
# print(result)

# 다른 사람 코드를 보지 않고 이전에 본 코드를 이해한것을 바탕으로 직접 짜본  코드.
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# temp = []
# result = 0
# for _ in range(n):
#     arr.append(int(input()))
# arr.append(0)
# temp.append((0, arr[0]))
#
# for i in range(1, n +1):
#     c = i
#     while temp and temp[-1][1] > arr[i]:
#         c, t = temp.pop()
#         result = max(result, t * (i - c))
#     temp.append((c, arr[i]))
# print(result)




# 다른사람의 풀이인데 실행시간이 짧고 메모리 사용 정도도 적어서 퍼와서 디버그를 돌리고 이해했다.
# import sys
#
# def solution():
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         arr.append(int(sys.stdin.readline()))
#
#     arr.append(0)
#     arr.insert(0, 0)
#     check = [0]
#     square = 0
#
#     for i in range(1, N+2):
#         while check and (arr[check[-1]] > arr[i]):
#
#             h = check.pop()
#             square = max(square, (i - 1 - check[-1]) * arr[h])
#         check.append(i)
#     print(square)
# solution()
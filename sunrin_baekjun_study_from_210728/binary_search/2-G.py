# https://www.acmicpc.net/problem/1300
# 시간초과한 풀이.
# from itertools import product
# from collections import deque
# N = int(input())
# k = int(input())
# arr = list(product([i for i in range(1, N+1)], [i for i in range(1, N+1)]))
# new_arr = deque()
#
#
# def compare_num(n):
#     start, end = 0, len(new_arr) - 1
#
#     goal = 1
#     while start <= end and new_arr:
#         mid = (start + end) // 2
#         if n < new_arr[mid]:
#             end = mid - 1
#             goal = mid
#         elif n > new_arr[mid]:
#             start = mid + 1
#             goal = mid + 1
#         else:
#             break
#     new_arr.insert(goal, n)
#
#
#     if len(new_arr) == k:
#         return True
#     return False
#
# ans = 0
#
# for i in range(len(arr)):
#     a, b = arr[i]
#     if compare_num(a * b):
#        ans = new_arr[-1]
#        break
#     continue
#
#
# print(ans)
#

# 다른 사람의 풀이를 보고 이해 후 작성
N = int(input())
k = int(input())
start, end = 1, k
ans = 0
while start <= end:
    mid = (start + end)//2
    temp = 0

    for i in range(1, N + 1):
        temp += min(N, mid//i)

    if temp < k:
        start = mid + 1
    elif temp >= k:
        ans = mid
        end = mid - 1
print(ans)


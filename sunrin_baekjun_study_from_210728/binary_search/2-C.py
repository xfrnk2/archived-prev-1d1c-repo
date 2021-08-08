# https://www.acmicpc.net/problem/2110

# 1회차 풀이 (혼자서 고민해보다가 결국 누군가 블로그의  풀이를 보고 이해하여 도움을 받아서 코드를 침)
# import sys
# n, c = map(int, input().split())
# house = [int(sys.stdin.readline()) for _ in range(n)]
#
# house = sorted(house)
# start, end = 1, house[-1] - house[0]
#
# def router_counter(distance):
#     cur_house = house[0]
#     count = 1
#     for i in range(1, n):
#         if cur_house + distance <= house[i]:
#             count += 1
#             cur_house = house[i]
#     return count
#
# ans = -1
# while start <= end:
#     mid = (start + end)//2
#     if router_counter(mid) < c:
#        end = mid - 1
#     else:
#         ans = mid
#         start = mid + 1
# print(ans)


# 2번째 풀이 ( 이것도 다른 곳에서 보고 이해후 코딩)
import sys
from bisect import bisect_left
n, c = map(int, input().split())
house = [int(sys.stdin.readline()) for _ in range(n)]

house = sorted(house)
start, end = 1, house[-1] - house[0]
ans = 0

while start <= end:
    count = 0
    mid = (start + end)//2
    idx = 0
    while idx < n:
        count += 1
        idx = bisect_left(house, house[idx] + mid)

    if count < c:
        end = mid - 1
    elif count >= c:
        start = mid + 1
        ans = mid

print(ans)
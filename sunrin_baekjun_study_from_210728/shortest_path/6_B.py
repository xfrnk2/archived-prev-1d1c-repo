# https://www.acmicpc.net/problem/7562
# 첫번째 풀이, 테케1에서 성공, 테케2에서 무한루프로 빠진다.
# N = int(input())
#
# for _ in range(N):
#     fl = int(input())
#     y, x = map(int, input().split())
#     ry, rx = map(int, input().split())
#     res = 0
#     que = [(y, x, 0)]
#     dy = [-1, 1, 2, 2, 1, -1, -2, -2]
#     dx = [-2, -2, -1, 1, 2, 2, 1, -1]
#     visited = [[0 for _ in range(fl)] for _ in range(fl)]
#     while que:
#         ly, lx, cnt = que.pop(0)
#         visited[ly][lx] = 1
#         if ly == ry and lx == rx:
#             res = cnt
#             break
#
#         for i in range(8):
#             if 0 <= ly + dy[i] < fl and 0 <= lx + dx[i] < fl:
#                 if visited[ly+dy[i]][lx+dx[i]] == 1:
#                     continue
#                 que.append((ly+dy[i], lx+dx[i], cnt + 1))
#     print(res)


#두번째 풀이
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

for _ in range(N):
    fl = int(input())
    y, x = map(int, input().split())
    ry, rx = map(int, input().split())

    que = deque()
    que.append((y, x))
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]
    dx = [-2, -2, -1, 1, 2, 2, 1, -1]

    graph = [[0] * fl for _ in range(fl)]
    while que:
        ly, lx = que.popleft()

        if ly == ry and lx == rx:
            break

        for i in range(8):
            ny, nx = ly+dy[i], lx+dx[i]
            if ny < 0 or fl <= ny or nx < 0 or fl <= nx:
                continue


            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[ly][lx] + 1
                que.append((ny, nx))
    print(graph[ry][rx])

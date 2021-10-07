# https://www.acmicpc.net/problem/2206
# 첫번째 풀이, 약 1시간 걸쳐 풀었는데 시간초과가 난다. 나올법한 반례는 잘 동작하는 듯 하는데, 더 잘 풀수 있는 방법이 뭘까? 고민해봐야겟다.
# import sys
# N, M = map(int, input().split())
# input = sys.stdin.readline
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
#
# field = []
#
# for _ in range(N):
#     field.append(list(map(int, input().strip())))
# queue = [((0, 0), 0)]
#
#
# while queue and field[N-1][M-1] == 0:
#     co, prev = queue.pop(0)
#     y, x = co
#     field[y][x] = prev + 1
#
#     if y == N-1 and x == M-1:
#         break
#
#     one_queue = []
#
#     t = 4
#     for k in range(4):
#         ny, nx = y + dy[k], x + dx[k]
#         if ny < 0 or nx < 0 or N <= ny or M <= nx:
#             t -= 1
#             continue
#
#
#
#         if field[ny][nx] == 0:
#             queue.append(((ny, nx), prev + 1))
#
#         else:
#             one_queue.append((ny, nx))
#
#     if one_queue and len(one_queue) == t:
#
#         for _ in range(len(one_queue)):
#             ty, tx = one_queue.pop(0)
#             prev -= 1
#             for k in range(4):
#                 ly, lx = ty + dy[k], tx + dx[k]
#                 if ly < 0 or lx < 0 or N <= ly or M <= lx:
#                     continue
#                 if field[ly][lx] == 0:
#                     queue.insert(0, ((ty, tx), prev + 2))
#
#
# if field[N-1][M-1] == 0:
#     print(-1)
# else:
#     print(field[N-1][M-1])

#두번재 풀이, 실패한다... 사실 이 전에 한번 풀이를 더 했으나 기록에 남기지 않는다. 다시 생각해보자.
# import sys
# N, M = map(int, input().split())
# input = sys.stdin.readline
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
# if N > M:
#     dy[0], dy[1] = dy[1], dy[0]
#     dx[0], dx[1] = dx[1], dx[0]
#
#
# field = []
# visited = [[1 for _ in range(M)]for _ in range(N)]
# for _ in range(N):
#     field.append(list(map(int, input().strip())))
# queue = [(0, 0, 0)]
# visited[0][0] = 1
#
# ans = 0
# while queue:
#
#     y, x, w = queue.pop(0)
#     if y == N-1 and x == M-1:
#         break
#
#     for i in range(4):
#         ny, nx = dy[i] + y , dx[i] + x
#         if ny < 0 or nx < 0 or N <= ny or M <= nx:
#             continue
#
#         # if visited[ny][ny] != 1:
#         #     continue
#         if w == 1 and field[ny][nx] == 1:
#             continue
#
#
#         if field[ny][nx] == 1:
#             visited[ny][nx] = visited[y][x] + 1
#             queue.append((ny, nx, w))
#
#         elif field[ny][nx] == 0:
#             visited[ny][nx] = visited[y][x] + 1
#             queue.append((ny, nx, w))
#
# for p in visited:
#     print(p)
# https://www.acmicpc.net/problem/2206
# 첫번째 풀이, 약 1시간 걸쳐 풀었는데 시간초과가 난다. 나올법한 반례는 잘 동작하는 듯 하는데, 더 잘 풀수 있는 방법이 뭘까? 고민해봐야겟다.

N, M = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

field = []

for _ in range(N):
    field.append(list(map(int, input())))
queue = [((0, 0), 0)]


while queue and field[N-1][M-1] == 0:
    co, prev = queue.pop(0)
    y, x = co
    field[y][x] = prev + 1

    if y == N-1 and x == M-1:
        break

    one_queue = []

    t = 4
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if ny < 0 or nx < 0 or N <= ny or M <= nx:
            t -= 1
            continue



        if field[ny][nx] == 0:
            queue.append(((ny, nx), prev + 1))

        else:
            one_queue.append((ny, nx))

    if one_queue and len(one_queue) == t:

        for _ in range(len(one_queue)):
            ty, tx = one_queue.pop(0)
            prev -= 1
            for k in range(4):
                ly, lx = ty + dy[k], tx + dx[k]
                if ly < 0 or lx < 0 or N <= ly or M <= lx:
                    continue
                if field[ly][lx] == 0:
                    queue.insert(0, ((ty, tx), prev + 2))


if field[N-1][M-1] == 0:
    print(-1)
else:
    print(field[N-1][M-1])

for j in range(N):
    print(field[j])
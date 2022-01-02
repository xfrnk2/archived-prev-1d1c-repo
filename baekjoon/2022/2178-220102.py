from collections import deque

N, M = map(int, input().split())
field = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution():
    graph = deque()
    graph.append((0, 0))
    while graph:
        x, y = graph.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or N - 1 < nx or ny < 0 or M - 1 < ny:
                continue
            if field[nx][ny] == 0:
                continue
            if field[nx][ny] == 1:
                graph.append((nx, ny))
                field[nx][ny] = field[x][y] + 1
    return field[N - 1][M - 1]


print(solution())

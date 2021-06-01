N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input())))

queue = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or N <= nx or M <= ny:
                continue
            if field[nx][ny] == 0:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = field[x][y] + 1
                queue.append((nx, ny))

    return field[N-1][M-1]

print(bfs(0, 0))
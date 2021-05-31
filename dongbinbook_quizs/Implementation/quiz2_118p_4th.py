N, M = map(int, input().split())
x, y, direction = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction += 1
    if 3 < direction:
        direction = 0

field[x][y] = 1
answer = 1
turn_count = 0

while turn_count < 5:
    for i in range(N):
        print(field[i])
    print('---')
    turn_left()
    turn_count += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if field[nx][ny] == 0:
        field[nx][ny] = 1
        x, y = nx, ny
        answer += 1
        turn_count = 0

print(answer)


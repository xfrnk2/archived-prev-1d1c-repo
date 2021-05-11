def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction

m, n = map(int, input().split())
x, y, direction = map(int, input().split())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
buffer = 0
c = 1
while True:
    print(field)
    direction = turn_left(direction)
    nx, ny = x + dx[direction], y + dy[direction]
    if field[nx][ny] == 0:
        x, y = nx, ny
        field[nx][ny] = 1
        c += 1
        continue
    buffer += 1
    if 4 <= buffer:
        nx, ny = x + dx[direction] * -1, y + dy[direction] * -1
        if field[nx][ny]== 1:
            break
        x, y = nx, ny
        buffer = 0



print(c)





'''
input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

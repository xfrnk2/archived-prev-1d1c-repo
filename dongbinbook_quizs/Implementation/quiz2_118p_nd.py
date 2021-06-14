n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)


'''
바다는 1, 육지는 0으로 구성되어있으며, N * M의 필드이다.
바라보는 방향(0 : 북, 1: 동, 2: 남, 3: 서) // 좌표는 x는 북쪽으로부터 떨어진 칸의 갯수, y는 서쪽으로부터 떨어진 칸의 갯수이다.
게임 캐릭터가 움직이는 것을 시뮬레이션 한다.

1. 왼쪽방향으로 회전한다.
2. 한칸 전진한 칸이 값이 0이면 이동시키고, 그게 아니라면 1번 과정으로 돌아간다.
3. 2번 과정에서 탐색한 4방향의 모든 칸을 이미 방문했거나, 바다(1)인지 확인한다. 조건을 만족하면 한 칸 뒤로 이동하는데, 이때 한 칸 뒤 칸이 바다라면 이동을 멈춘다.
4. 3번의 확인 조건을 만족하지 못하면 1로 되돌아간다.

input
4 4 // N M
1 1 0 // 현재 x, 현재 y좌표, 바라보는 방향은 북쪽
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

output
3

'''
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
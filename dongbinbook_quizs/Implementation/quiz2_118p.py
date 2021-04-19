# 1회차 풀이
# 감상 : 나중에 visited_count를 1 추가하다니 어딘가 모자라 보이는 구성이지 않은가? 다시 도전해서 더 좋은 코드를 만들어 보자.


direction_hash = {0: (0, -1), 1:(1, 0), 2:(0, 1), 3:(-1, 0)}


N, M = map(int, input().split())
status = list(map(int, input().split()))
field = [list(map(int, input().split())) for _ in range(N)]
row, col, current_direction = status[0], status[1], status[2]
visited = 2

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
visited_count = 0
turn_count = 0


while True:
    current_direction -= 1
    if current_direction < 0:
        current_direction = 3

    if 3 < turn_count:
        visited_count += 1
        dx, dy = direction_hash[current_direction]
        if field[row + dx * -1][col +  dy * -1] == 1:
            break

        row, col = row + dx * -1, col + dy * -1
        turn_count = 0
        continue


    dx, dy = direction_hash[current_direction]
    new_row, new_col = row + dx, col + dy

    if field[new_row][new_col] == 0:
       visited_count += 1
       field[row][col] = visited
       turn_count = 0
       row, col = new_row, new_col
       continue
    turn_count += 1

print(visited_count)





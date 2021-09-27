# https://www.acmicpc.net/problem/4963

# 중앙 기준 시계방향으로 0시~12시로 이동
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


# 사실상 두번째 풀이. 지난번 첫번째 풀이 시도때에는 알바후 몸이 피곤해서였는지 1시간 20분을 들여도 실패해서 풀이를 멈췄었다.
# 이번에는 비교적 컨디션이 좋은 상태에서 풀이에 임하니 20분만에 풀어버리는 사태가 되었다. (...)
# 문제 풀이는 컨디션 상태에 영향을 많이 받는구나 싶었다.

while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    #필드, 방문여부 확인을 위한 배열생성
    field = []
    visited = [[0 for _ in range(w)]for _ in range(h)]
    for n in range(h):
        field.append(list(map(int, input().split())))

    count = 0



    for k in range(h):
        for j in range(w):

            if field[k][j] == 0:
                continue

            if visited[k][j] == 1:
                continue

            queue = [(k, j)]
            visited[k][j] = 1
            while queue:
                y, x = queue.pop(0)
                for i in range(8):
                    ny, nx = y + dy[i], x + dx[i]
                    if ny < 0 or nx < 0 or h <= ny or w <= nx:
                        continue

                    if visited[ny][nx] == 1:
                        continue
                    else:
                        if field[ny][nx] == 1:
                            queue.append((ny, nx))

                        visited[ny][nx] = 1
            if field[k][j] == 1:
                count += 1
    print(count)



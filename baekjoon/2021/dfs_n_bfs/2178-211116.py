# https://www.acmicpc.net/problem/2178
N, M = map(int, input().split())
F = [list(map(int, input())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # x는 행, y는 열

def solution():
    answer = 10e5
    def dfs(x, y, c):
        nonlocal answer

        if x == N - 1 and y == M - 1:
            answer = min(answer, c)
            return

        F[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or N <= nx or M <= ny or F[nx][ny] == 0:
                continue
            dfs(nx, ny, c + 1)



    dfs(0, 0, 1)
    return answer


print(solution())
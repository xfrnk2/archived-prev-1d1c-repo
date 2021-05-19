N, M = map(int, input().split())
coordinate = [list(map(int, input())) for _ in range(N)]
print(coordinate)

def dfs(x, y):
    if x < 0 or y < 0 or N <= x or M <= y:
        return False
    if coordinate[x][y] == 1:
        return False
    coordinate[x][y] = 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    return True



result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1
print(result)

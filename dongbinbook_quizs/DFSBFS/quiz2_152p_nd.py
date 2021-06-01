N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input())))


def dfs(x, y, prev_value):
    for i in range(N):
        print(field[i])
    if x < 0 or y < 0 or N <= x or M <= y:
        return False
    if field[x][y] == 1:
        field[x][y] = prev_value + 1

        group = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        v = field[x][y]
        for item in group:
            i, j = item
            dfs(i, j, v)

        return True

    return False
dfs(0, 0, 0)

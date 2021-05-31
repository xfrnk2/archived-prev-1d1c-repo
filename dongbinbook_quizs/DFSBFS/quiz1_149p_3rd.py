N, M = map(int, input().split())
field = []

for _ in range(N):
    field.append(list(map(int, input())))

print(field)
def dfs(x, y):
    if x < 0 or y < 0 or N <= x or M <= y:
        return False

    if field[x][y] == 0:
        field[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

answer = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            answer += 1
print(answer)


'''
4 5
00110
00011
11111
00000
'''
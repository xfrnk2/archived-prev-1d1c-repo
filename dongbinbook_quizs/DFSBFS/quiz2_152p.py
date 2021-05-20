N, M = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input())))

def bfs(x, y, prev_value):
    if x < 0 or y < 0 or N <= x or M <= y:
        return False

    if field[x][y] == 0:
        return False

    if field[x][y] == 1:
        field[x][y] += prev_value

        v = field[x][y]

        bfs(x + 1, y, v)
        bfs(x - 1, y, v)
        bfs(x, y + 1, v)
        bfs(x, y - 1, v)
        return True
    return False

bfs(0, 0, 0)

print(field[N-1][M-1])

for i in range(N):
    print(field[i])

'''
5 6
101010
111111
000001
111111
111111
'''
n:int = 8
maze = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0],
    ]
pathway = 0
wall = 1
blocked = 2
path = 3

def func(x, y):
    if x < 0 or y < 0 or n-1 < x or n-1 < y:
        return False
    elif maze[x][y] != pathway:
        return False
    elif x == n-1 and y == n-1:
        print("success")
        maze[x][y] = path
        return True
    else:
        maze[x][y] = path
        if func(x - 1, y) or func(x, y - 1) or func(x + 1, y) or func(x, y + 1): #서-남-동-서 방향으로 순회
            return True
        maze[x][y] = blocked
        return False




for x in maze:
    print(x)
func(0,0)
print('\ㅜ')
for x in maze:
    print(x)

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

def func(x:int, y:int):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif maze[x][y] != pathway:
        return False
    elif x== n-1 and y==n-1:
        maze[x][y] = path
        print("success")
        return True
    else:
        maze[x][y] = path
        if func(x-1, y) or func(x, y+1) or func(x+1, y) or func(x, y-1): #북-동-남-서 방향으로 순회
            return True
        maze[x][y] = blocked
        return False


if __name__ == '__main__':

    func(0, 0)
    for x in maze:
        print(x)

#재귀를 통해서 모든 방향의 연결된 imaged_pixel의 갯수를 카운팅하여 반환하는 함수를 구현하였다.


n = 8
already_checked = 2
imaged_pixel = 1
background = 0
grid = [
    [1,0,0,0,0,0,0,1],
    [0,1,1,0,0,1,0,0],
    [1,1,0,0,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,0],
    [1,0,0,0,1,0,0,1],
    [0,1,1,0,0,1,1,1]
]
def func(x, y):
    if x < 0 or y < 0 or n-1 < x or n-1 < y:
        return False
    if grid[x][y] != imaged_pixel:
        return False
    else:
        grid[x][y] = already_checked
        return 1+ func(x-1, y) + func(x-1, y+1) + func(x, y+1) + func(x+1, y+1) + func(x+1, y) + func(x+1, y-1) + func(x, y-1) + func(x-1, y-1)







if __name__ == '__main__':

    for x in grid:
        print(x)
    print(func(5, 3))

    for x in grid:
        print(x)

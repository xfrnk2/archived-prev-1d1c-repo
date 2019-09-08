import copy
def cavityMap(grid):
    length = len(grid)
    if length < 3:
        return grid

    grid = [list(x) for x in grid]

    r = copy.deepcopy(grid)

    for i in range(1, length - 1):
        for j in range(1, length - 1):
            if all(int(grid[i][j]) > int(grid[k][l]) for k, l in
                   [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]):
                r[i][j] = 'X'

    for x in r:
        x = [str(value) for value in x]

        x = ''.join(x)
    return r
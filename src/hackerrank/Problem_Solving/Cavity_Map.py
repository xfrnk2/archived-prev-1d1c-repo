import copy
import itertools
def cavityMap(grid):
    length = len(grid)
    if length < 3:
        return grid

    grid = [list(x) for x in grid]

    r = copy.deepcopy(grid)

    for i, j in itertools.product(range(1, length - 1), range(1, length - 1)):
            if all(int(grid[i][j]) > int(grid[k][l]) for k, l in
                   [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]):
                r[i][j] = 'X'

    result = [''.join(map(str, x)) for x in r]
    ''.join(result)

    return result

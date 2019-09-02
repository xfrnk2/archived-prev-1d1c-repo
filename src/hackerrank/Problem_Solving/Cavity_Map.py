
def cavityMap(grid):
    if len(grid) <= 2:
        return grid
    v = 0
    f = True
    grid_ = grid[1:-1]

    for j in grid_:
        if f:
            if len(j) <= 2:
                return grid
            f = False

        max_value = int(max(j))
        if v < max_value:
            v = max_value
    v = str(v)

    result = [grid[0], grid[-1]]
    n = 1
    for x in grid_:
        t = x[1:-1]

        result.insert(n, x[0] + t.replace(v, "X") + x[-1])
        n += 1

    ''.join(result)

    return result

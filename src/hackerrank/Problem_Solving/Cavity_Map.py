def cavityMap(grid):
    g_length = len(grid)
    j_length = 0
    value = 0

    if g_length <= 2:
        return grid

    for i, j in enumerate(grid):
        j_length = len(j)
        if i == 0:
            if j_length <= 2:
                return grid

        for x in j[1:-1]:
            if value < x:
                value = x
    return grid

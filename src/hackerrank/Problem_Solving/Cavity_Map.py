def cavityMap(grid):
    v = 0
    for x in grid:
        p = int(max(x))
        if v < p:
            v = p

    map_l = [x.replace(str(v), 'X') for x in grid]

    return map_l
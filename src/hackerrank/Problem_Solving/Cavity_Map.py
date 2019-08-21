def cavityMap(grid):
    if len(grid) <= 2 or len(grid[0]) <= 2:
        return grid

    box = []
    x_value = grid[1:-1]
    target = 0

    for x in x_value:
        box.extend(x[1:-1])
    target = max(box)

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):

            if grid[x][y] == target:
                pass
    return grid
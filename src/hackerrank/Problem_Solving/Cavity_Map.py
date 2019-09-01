def cavityMap(grid):
    if not 2 < len(grid):
        return grid

    valuebox = []
    for z in grid[1:-1]:
        if not 2 < len(z):
            return grid

        for y in z[1:-1]:
            valuebox += y
    max_value = max(valuebox)

    box = []
    for a, x in enumerate(grid):
        value = x
        if a == 0 or a == len(grid) - 1:
            pass
        else:
            for i, j in enumerate(x):

                if i == 0 or i == len(x) - 1:
                    continue
                if j == max_value:
                    value = x[:i] + 'X' + x[i + 1:]

        box.append(value)
    return box

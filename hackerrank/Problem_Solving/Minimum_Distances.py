import sys

def minimumDistances(a):
    if len(a) == 1:
        return -1

    box = {}
    for i, j in enumerate(a):
        if j not in box:
            box[j] = [1, [i]]
        else:
            box[j][0] += 1
            box[j][1].append(i)

    if not list(filter(lambda x: 2 <= x[0], box.values())):
        return -1

    result = min_distance = sys.maxsize

    for y in box.values():

        if y[0] < 2:
            continue

        for i, z in enumerate(y[1]):
            if i == 0:
                continue
            distance = abs(z - y[1][i - 1])

            if distance < min_distance:
                min_distance = distance

        if min_distance < result:
            result = min_distance

    return (result)

import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    length = len(a)
    minDist = -1

    if length == 1:
        return minDist

    for x in range(length):
        for y in range(x + 1, length):
            if a[x] == a[y]:
                if minDist == -1:
                    minDist = y - x
                else:
                    if y - x < minDist:
                        minDist = y - x

    return minDist

import sys


# Complete the minimumDistances function below.
def minimumDistances(a):
    minDist = sys.maxsize
    index_box = {}
    for i, j in enumerate(a):
        if j in index_box:
            minDist = min(minDist, i - index_box[j])
        index_box[j] = i
    return minDist if minDist != sys.maxsize else -1
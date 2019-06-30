from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    box = Counter(arr)

    size = 0

    maxValue = 0

    for value in box.values():

        size += value

        if maxValue < value:
            maxValue = value

    return size - maxValue
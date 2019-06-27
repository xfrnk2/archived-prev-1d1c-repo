from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    box = Counter(arr)

    size = 0

    maxValue = 0

    for x in box:

        size += box[x]

        if maxValue < box[x]:
            maxValue = box[x]

    return size - maxValue

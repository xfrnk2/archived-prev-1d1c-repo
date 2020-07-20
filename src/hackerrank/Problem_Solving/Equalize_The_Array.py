from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):

    box = Counter(arr)

    size = 0

    max_value = 0

    for value in box.values():

        size += value

        max_value = max(max_value, value)

    return size - max_value

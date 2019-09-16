def fairRations(arr):
    length = len(arr)
    count = 0

    for x in range(length - 1, 0, -1):
        if arr[x] % 2 == 1:
            arr[x], arr[x - 1] = arr[x] + 1, arr[x - 1] + 1
            count += 2

    if arr[0] % 2 == 1:
        return "NO"

    return count
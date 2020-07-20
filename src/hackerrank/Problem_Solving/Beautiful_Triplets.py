def beautifulTriplets(d, arr):
    count = 0
    if d == 0 or arr == []:
        return count

    for i, j in enumerate(arr):
        if i == len(arr) - 2:
            break
        if j + d in arr[i:] and j + d + d in arr[i:]:
            count += 1
    return count


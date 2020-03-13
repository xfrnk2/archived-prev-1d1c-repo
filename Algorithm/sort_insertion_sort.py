def insertion_sort(arr):
    for idx in range(1, len(arr)):
        temp = arr[idx]
        temp_idx = idx
        while arr[temp_idx-1] > temp:
            arr[temp_idx] = arr[temp_idx-1]
            temp_idx -= 1
            if temp_idx == 0:
                break
        arr[temp_idx] = temp
    return arr
print(insertion_sort([1, 4, 3, 2, 10]))
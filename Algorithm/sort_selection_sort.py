def selection_sort(arr):
    length = len(arr)

    for i in range(0, length-1):
        least_index = i
        for j in range(i+1, length):
            if arr[j] < arr[least_index]:
                least_index = j

        if arr[least_index] != arr[i]:
            arr[i], arr[least_index] = arr[least_index], arr[i]

    return arr

print(selection_sort([5,2,3,4,1, 14, 20, 255, 30]))




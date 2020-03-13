def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)

def another_range(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)



bubble_sort([3, 9, 5, 2])
another_range([3, 9, 5, 2, 100, 1])
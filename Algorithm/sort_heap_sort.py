def heapify(arr, i):
    index = i+1

    if index*2 > len(arr):
        #자식 없음
        return
    elif index*2 == len(arr):
        #왼쪽 노드만 있음
        k = arr[index*2-1]
        if arr[i] < k:
            arr[i], arr[index*2-1] = arr[index*2-1], arr[i]
            return

    k = arr[index*2-1]
    if k < arr[index*2]:
        if arr[i] < arr[index*2]:
            arr[i], arr[index*2] = arr[index*2], arr[i]
            return heapify(arr, index*2-1)

    else:
        if arr[i] < arr[index*2-1]:
            arr[i], arr[index*2-1] = arr[index*2-1], arr[i]
            return heapify(arr, index*2-2)

arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
heapify(arr, 0)
print(arr)

def heap_sort(arr):
    size = len(arr)-1
    while 0 < size:

        arr[0], arr[size] = arr[size], arr[0]
        size -= 1
        heapify(arr, 0)


heap_sort(arr)
print(arr)







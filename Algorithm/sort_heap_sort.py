def heapify(arr, i):
    index = i+1

    if index*2 > len(arr):
        #자식 없음
        return heapify(arr, (i+1)//2-1)
    elif index*2 == len(arr):
        #왼쪽 노드만 있음
        k = arr[index*2-1]
        if arr[i] < k:
            arr[i], arr[index*2-1] = arr[index*2-1], arr[i]
            return arr


    k = arr[index*2-1]
    if k < arr[index*2]:
        if arr[i] < arr[index*2]:
            arr[i], arr[index*2] = arr[index*2], arr[i]
            return heapify(arr, index * 2)
        else:
            return
    else:
        if arr[i] < arr[index*2-1]:
            arr[i], arr[index*2-1] = arr[index*2-1], arr[i]
            return heapify(arr, index*2-1)
        else:
            return


arr = [15, 3, 16, 4, 2]
heapify(arr, len(arr)-1)
print(arr)
def partiton(arr, left, right):
        p, q, k = left, left+1, arr[left]

        while q <= right:
            if arr[q] < k:
                p += 1
                arr[p], arr[q] = arr[q], arr[p]
            q += 1
        arr[p], arr[left] = arr[left], arr[p]
        return p


def quickSort(arr, left, right):
    if left < right:
        pivot = partiton(arr, left, right)
        quickSort(arr, left, pivot-1)
        quickSort(arr, pivot+1, right)
arr = [-2, 11, 3, 1, 2, 100, 9, 0, 77 ,2, 45,-33, 100]
quickSort(arr, 0, len(arr)-1)
print(arr)
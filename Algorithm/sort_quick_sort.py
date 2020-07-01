arr = [100, 22, 55, 12, 0, 150, 12]
length = len(arr)

def quick_sort(arr, p, q):

    if p < q:
        pivot = partition(arr, p, q)
        quick_sort(arr, p, pivot-1)
        quick_sort(arr, pivot+1, q)

def partition(arr, p, q):
    i, j, k = p-1, p, arr[q]
    while j < q:
        if arr[j] < k:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            j+=1
        
    arr[i+1], arr[q] = arr[q], arr[i+1]
    return i+1

quick_sort(arr, 0, length-1)
print(arr)
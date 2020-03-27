arr = [60, 200, 30, 0, 250, 70, 11]
length = len(arr)
def quick_sort(arr, p, q):
    if p < q:
        pivot = partition(arr, p, q)
        quick_sort(arr, p, pivot-1)
        quick_sort(arr, pivot+1, q)

def partition(arr, p, q):
    i, j, k = p, p+1, arr[p]
    while j <= q:
        if arr[j] < k:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
    arr[i], arr[p] = arr[p], arr[i]
    return i
quick_sort(arr, 0, len(arr)-1)
print(arr)
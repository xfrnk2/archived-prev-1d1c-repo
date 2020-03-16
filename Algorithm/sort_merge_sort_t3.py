#다른 방식으로 풀기
arr = [5, 4, 3, 2, 1, 0]
length = len(arr)


def divide(arr, p, q):
    if p < q:
        m = (p+q) // 2
        divide(arr, p, m)
        divide(arr,m+1, q)
        print(arr)
        return merge(arr, p, m, q)

def merge(arr, p, m, q):
    i, j, k = p, m+1, p
    temp = ['' for x in range(length)]
    while i <= m and j <= q:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k, i = k+1, i+1
        else:
            temp[k] = arr[j]
            k, j = k + 1, j + 1
    while i <= m:
        temp[k] = arr[i]
        k, i = k + 1, i + 1
    while j <= m:
        temp[k] = arr[j]
        k, j = k + 1, j + 1
    for i in range(p, q+1):
        arr[i] = temp[i]


divide(arr, 0, length-1)
print(arr)
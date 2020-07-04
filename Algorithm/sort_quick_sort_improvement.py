from random import randrange
arr = [-2, 11, 3, 1, 2, 100, 9, 0, 77 ,2, 45,-33, 100]
arr2 = [-2, 11, 3, 1, 2, 100, 9, 0, 77 ,2, 45,-33, 100]
# 1. 피벗을 난수로


def partiton(arr, left, right):
    randNum = randrange(left, right+1)
    arr[randNum], arr[left] = arr[left], arr[randNum]
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

quickSort(arr, 0, len(arr)-1)
print(arr)

# 2. 세 값의 중위

def medianOfThree(arr, start, end):
    mid = (end+start)//2

    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]

    arr[mid], arr[start] = arr[start], arr[mid]


def partiton2(arr, left, right):
    medianOfThree(arr, left, right)

    p, q, k = left, left+1, arr[left]

    while q <= right:
        if arr[q] < k:
            p += 1
            arr[p], arr[q] = arr[q], arr[p]
        q += 1
    arr[p], arr[left] = arr[left], arr[p]
    return p


def quickSort2(arr, left, right):
    if left < right:
        pivot = partiton2(arr, left, right)
        quickSort2(arr, left, pivot-1)
        quickSort2(arr, pivot+1, right)


quickSort2(arr2, 0, len(arr2)-1)
print(arr2)
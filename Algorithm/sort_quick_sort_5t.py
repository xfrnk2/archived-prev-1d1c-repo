arr = [100, 22, 55, 12, 0, 150, 12]
length = len(arr)
# 참고로 한 괜찮은 설명 : https://coding-factory.tistory.com/137

def partition(arr, start, end):
    pivot = arr[start]
    left, right = start+1, end
    while left <= right:
        while left <= end and pivot >= arr[left]:
            left += 1
        while start+1 <= right and pivot <= arr[right]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quickSort(arr, start, end):
    if start <= end:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1)
        quickSort(arr, pivot+1, end)

quickSort(arr, 0, len(arr)-1)
print(arr)
'''

배열의 가장 왼쪽, 오른쪽, 중간 값 3개를 사용합니다.

세 값을 정렬하여 가장 작은 값을 가장 왼쪽에 중간값을 중간에 가장 큰 값을 가장 오른쪽으로 이동시킵니다.

이 후 중간값을 가장 오른쪽의 앞과 변경합니다.

이렇게 되면, 배열의 첫번째 값은 마지막의 앞의 값보다 항상 작고, 마지막 값은 마지막 앞의 값보다 항상 크기 때문에 분할 구간이 좁혀지게 됩니다.

위처럼 범위를 2개 줄이게 되면 재귀의 깊이(반복횟수)도 줄일 수 있으므로 피벗선택이 효율적으로 이루어진다고  볼 수 있습니다.

위의 글을 많은 블로그에서 완전히 똑같은 형태로 많이 봤는데, 구현을 어떻게 하면 좋은지 감을 못 잡아서 찾아본 결과
https://stackoverflow.com/questions/7559608/median-of-three-values-strategy
결론 : 모든 과정에 적용하는것이 아닌지 착오가 있었던 것을 알게 되었다. 생각 이상으로 단순했는데,
그냥 함수의 동작 수행과정의 가장 처음부분에서 가장 앞의 원소, 중간의 원소, 가장 뒤의 원소를 비교해서 정렬하여 나온 median 값을
pivot으로 삼으면 되는 것이었다.
'''


# def getMedian(arr, start, end):
#     mid = (end-start)//2
#
#     if arr[start] > arr[end]:
#         arr[start], arr[end] = arr[end], arr[start]
#     if arr[start] > arr[mid]:
#         arr[start], arr[mid] = arr[mid], arr[start]
#     if arr[mid] > arr[end]:
#         arr[mid], arr[end] = arr[end], arr[mid]
#     return mid
#
# def partition(arr, start, end):
#
#         pivot = getMedian(arr, start, end)
#
#         i, j, pivot_value = start, end, arr[pivot]
#         while i < pivot and j > pivot:
#             while arr[i] < pivot_value:
#                 i += 1
#             while pivot_value < arr[j]:
#                 j -= 1
#             if i <= j:
#                 arr[i], arr[j] = arr[j], arr[i]
#             if start <= pivot or pivot <= end:
#                 arr[start], arr[end] = arr[end], arr[start]
#             arr[start], arr[end] = arr[end], arr[start]
#             return right
# def quickSort(arr, start, end):
#     if start <= end:
#         pivot = partition(arr, start, end)
#         quickSort(arr, start, pivot - 1)
#         quickSort(arr, pivot+1, end)
#
#
#
# arr = [2, 4, 1, 5, 7, 6, 9, 8, 0, 14]
# quickSort(arr, 0, len(arr)-1)
# print(arr)

arr = [100, 22, 55, 12, 0, 150, 12]
length = len(arr)
# 참고로 한 괜찮은 설명 : https://coding-factory.tistory.com/137

def setMedian(arr, start, end):
    mid = (end-start)//2

    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]

    arr[mid], arr[start] = arr[start], arr[mid]

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

setMedian(arr, 0, len(arr)-1)
quickSort(arr, 0, len(arr)-1)
print(arr)
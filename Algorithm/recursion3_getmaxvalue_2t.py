def sequential_search(begin, end, arr, target):
    if begin > end:
        return -1
    if arr[begin] == arr[target]:
        return begin
    return sequential_search(begin + 1, end, arr, target)
print(sequential_search(0, 4, [1, 2, 3, 4, 5], 4))

def binary(begin, end, arr, target):
    if begin > end:
        return -1
    else:
        middle = (begin + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            return binary(middle+1, end, arr, target)
        else:
            return binary(begin, middle-1, arr, target)
print(binary(0, 4,[1, 5, 10, 15, 20], 20))

def maxvalue(begin, end, arr):
    if begin == end:
        return arr[begin]
    else:
        return max(arr[begin], maxvalue(begin+1, end, arr))

def maxvalue2(begin, end, arr):
    if begin == end:
        return arr[end]
    else:
        return max(arr[end], maxvalue2(begin, end-1, arr))

def maxvalue3(begin, end, arr):
    if begin == end:
        return arr[begin]
    else:
        middle = (begin + end) //2
        max1 = maxvalue3(begin, middle, arr)
        max2 = maxvalue3(middle+1, end, arr)
        return max(max1, max2)

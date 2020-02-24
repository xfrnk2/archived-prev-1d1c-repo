def func1(arr: list, begin: int, end: int):
    if begin == end:
        return arr[begin]
    else:
        return max(arr[begin], func1(arr, begin+1, end))

print(func1([5, 4, 3, 2, 1], 0, 4))

def func2(arr: list, begin: int, end: int):
    if begin == end:
        return arr[end]
    else:
        return max(arr[end], func2(arr, begin ,end-1))
print(func2([6, 4, 3, 1, 7], 0, 4))

def func3(arr: list, begin: int, end: int):
    if begin == end:
        return arr[begin]
    else:
        middle = (begin+end)//2
        max1 = func3(arr, begin, middle)
        max2 = func3(arr, middle+1, end)
        return max(max1, max2)
print(func3([3, 100, 1, 2, 125], 0, 4))

def binary(arr: list, begin: int, end: int, target: int):
    if begin > end:
        return
    else:
        middle = (begin+end)//2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            return binary(arr, begin, middle-1, target)
        else:
            return binary(arr, middle+1, end, target)
print(binary([1, 5, 10, 15, 20], 0, 4, 20))




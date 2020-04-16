#quick_sort를 pythonic하게 구현한다.
def quick_sort(arr):
    pivot = len(arr)//2
    if 0 < pivot:
        left, right = [], []
        for x in arr:
            if x == arr[pivot]:
                continue
            if x < arr[pivot]:
                left.append(x)
            elif x > arr[pivot]:
                right.append(x)
        v1 = quick_sort(left)
        v2 = quick_sort(right)
        return v1+[arr[pivot]]+v2
    else:
        return arr
arr = [5, 4, 3, 2, 1, 100, 25, 3, 1, 100]
print(quick_sort(arr))

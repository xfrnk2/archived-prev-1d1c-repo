#랜덤한 원소를 기준으로 퀵 정렬을 pythonic하게 구현한다.
#새로운 리스트를 만들지 않고 구현한다.
from random import randrange
def quick_sort(arr, lhs, rhs):
    pivot = randrange(len(arr)-1)
    left, right = lhs, rhs
    if lhs < rhs:
        while left < pivot:
            left+=1
        while right > pivot:
            right-=1

        if left != right :
            if lhs + 1 == left:
                arr[lhs], arr[right] = arr[right], arr[lhs]
                return quick_sort(arr, left, rhs)
            elif rhs - 1 == right:
                arr[left], arr[rhs] = arr[rhs], arr[left]
                return quick_sort(arr, lhs, right)
            else:
                while lhs <= rhs:
                    left +=1
                    right -=1
                    quick_sort(arr, left, right)
        else:
            arr[lhs], arr[rhs] = arr[rhs], arr[lhs]
            return quick_sort(arr, lhs+1, rhs-1)
arr = [1, 100, 250, 1, 0]

quick_sort(arr, 0, len(arr)-1)
print(arr)
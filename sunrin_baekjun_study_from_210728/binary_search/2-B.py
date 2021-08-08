# https://www.acmicpc.net/problem/10816

def bisect_l(arr, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_r(arr, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo

n = int(input())
numbers = sorted(list(map(int, input().split())))
input()
targets = list(map(int, input().split()))


for t in targets:
    print(bisect_r(numbers, t) - bisect_l(numbers, t), end=' ')

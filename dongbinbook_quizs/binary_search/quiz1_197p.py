import sys
r_input = sys.stdin.readline
N = int(input())
components = list(map(int, r_input().split()))
components.sort()
M = int(input())
targets = list(map(int, r_input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False



for num in targets:
    if binary_search(components, num, 0, N-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')


'''
input
5
8 3 7 9 2
3
5 7 9

output
no yes yes
'''

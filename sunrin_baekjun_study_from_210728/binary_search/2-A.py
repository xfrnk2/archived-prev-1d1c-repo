# https://www.acmicpc.net/problem/1920
input()
arr = sorted(list(map(int, input().split())))
n = int(input())
targets = list(map(int, input().split()))


# 시간초과남..
# result = ''
# for target in targets:
#     s, e = 0, n-1
#     flag = False
#     while s <= e:
#         mid = (s + e) // 2
#         if target == arr[mid]:
#             flag = True
#             break
#
#         if target < arr[mid]:
#             e = mid
#         else:
#             s = mid + 1
#
#     result += str(int(flag))
#
#
#
# print(result)


n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, val, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, high)
    elif arr[mid] > val:
        return binary_search(arr, val, low, mid-1)
    else:
        return True


for target in targets:
    print(int(binary_search(arr, target, 0, n-1)))


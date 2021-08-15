# https://www.acmicpc.net/problem/12931
# 첫 번째 풀이.
N = int(input())
arr = list(map(int, input().split()))

count = 0
while any(arr):
    flag = True
    target = None
    for i in range(len(arr)):

        if arr[i] % 2 == 1:
            flag = False
            target = i

    if flag:
        for j in range(len(arr)):
            arr[j] //= 2
    else:
        arr[target] -= 1

    count += 1
print(count)



# 두 번째 풀이. 그런데 왜 틀렸을까?
# N = int(input())
# arr = list(map(int, input().split()))
#
# count = 0
# while any(arr):
#
#     target = None
#     for i in range(len(arr)):
#
#         if arr[i] % 2 == 1:
#
#             target = i
#
#     if not target:
#         for j in range(len(arr)):
#             arr[j] //= 2
#     else:
#         arr[target] -= 1
#
#     count += 1
# print(count)
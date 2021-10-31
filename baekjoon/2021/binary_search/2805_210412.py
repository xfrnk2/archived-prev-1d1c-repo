# https://www.acmicpc.net/problem/2805
# num, value = list(map(lambda x: int(x), input.split()))
# arr = input.split()


# def func(arr, low_value, max_value, target):  # 초기의 middle_value와 target은 같음
#     '''
#     1. 해당 범위내 중간값을 정한다 -> m_value
#     2. 전체 배열에서 중간값을 뺀 값이 0 이상 양수인 것만으로 이루어진 또다른 배열의 값들을 모두 더한 값이 중간 값과 어떤 관계인지 비교한다.
#     '''
#     m_value = max_value - (max_value - low_value) // 2
#     a = sum([x - m_value for x in arr if m_value < x])
#     if a == target:
#         print(m_value)
#         return
#     elif a < target:  # 더 내려가야됨
#         func(arr, low_value, m_value, target)
#     elif a > target:
#         func(arr, m_value, max_value, target)
#
#
# num, target_value = list(map(lambda x: int(x), input().split()))
# arr = list(map(lambda x: int(x), input().split()))
# func(arr, max(arr) - target_value, max(arr), target_value)
n, target = list(map(lambda x: int(x), input().split()))
arr = list(map(lambda x: int(x), input().split()))

max_value = max(arr)
low_value = max_value - target
target_temp = target//2
middle_value = low_value + target_temp
answer = 0
while True:
    s = sum([x - middle_value for x in arr if middle_value < x])
    if s == target:
        answer = middle_value
        break
    if s < target:
        max_value = middle_value
    elif s > target:
        low_value = middle_value
    middle_value = max_value - target_temp // 2
print(middle_value)

'''
Input:
4 7
20 15 10 17

Output:
15
Input:
5 20
4 42 40 26 46

Output:
36
'''

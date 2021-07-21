# def f(s):
#     score = list(map(int, s))
#     mid = len(score)//2
#     left, right = 0, 0
#     is_not_changed = True
#
#     for i in range(len(score)):
#         if is_not_changed and mid <= i:
#             left, right, is_not_changed = right, 0, False
#         right += score[i]
#     if left == right:
#         return "LUCKY"
#     return "READY"
#
# print(f(input()))


# 더 좋은 풀이가 있어서 참고해서 수정해봄.
def f(s):
    score = list(map(int, s))
    sum_left, sum_right = 0, 0
    for i in range(len(score)//2):
        sum_left += score[i]
        sum_right += score[len(score) - i - 1]

    if sum_left == sum_right:
        return "LUCKY"
    return "READY"

print(f(input()))
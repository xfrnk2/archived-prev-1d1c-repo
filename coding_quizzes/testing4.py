import random


# def set_page():
#     pobi = []
#     crong = []
#
#
#
#     for name in pobi, crong:
#         while True:
#             page = random.randrange(3, 397)
#             if page % 2 != 1:
#                 continue
#             else:
#                 name.append(page)
#                 name.append(page + 1)
#                 break
#     print(pobi)
#     print(crong)
# set_page()

import random
pobi = [3, 4]
crong = [5, 6]

def solution(pobi, crong):
    answer = ''
    if pobi[0] + 1 != pobi[1] or crong[0] + 1 != crong[1]:
        answer = -1
        return answer

    group = [pobi, crong]
    p_values = []
    c_values = []

    for name in group:
        add_value = 0
        mul_value = 1
        if len(name) != 2:
            answer = -1
            return answer

        for numbers in name:
            numbers = str(numbers)
            for number in numbers:
                add_value += int(number)
                mul_value *= int(number)

        if name == pobi:
            p_values.append(add_value)
            p_values.append(mul_value)
        else:
            c_values.append(add_value)
            c_values.append(mul_value)

    p = max(p_values)
    c = max(c_values)

    if p > c:
        answer = 1
    if p < c:
        answer = 2
    if p == c:
        answer = 0

    return answer


print(solution(pobi, crong))

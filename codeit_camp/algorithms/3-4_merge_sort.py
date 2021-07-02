# 복잡하게 풀었다. 단순하게 풀자.
# def divide(data):
#     print('data', data)
#     mid = len(data) // 2
#     if 1 < len(data):
#         arr = []
#         lhs, rhs = divide(data[:mid]), divide(data[mid:])
#         print('lhs와 rhs', lhs, rhs)
#         while (lhs and rhs):
#             print('while')
#             if lhs[0] > rhs[0]:
#                 arr.append(rhs.pop(0))
#             else:
#                 arr.append(lhs.pop(0))
#         print('남은 lhs rhs', lhs, rhs)
#         arr.extend((lhs + rhs))
#         print('완료', arr, data)
#         return arr
#     else:
#         return data


# def divide(listdata):

#     mid = len(listdata) // 2
#     lhs, rhs = listdata[:mid], listdata[mid:]
#     return lhs, rhs


# def conquer(list1, list2):
#     arr = []
#     while list1 and list2:
#         if list1[0] > rhs[0]:
#             arr.append(rhs.pop(0))
#         else:
#             arr.append(lhs.pop(0))
#     arr.extend((lhs + rhs))
#     return arr

def divide(data):
    mid = len(data) // 2
    if 1 < len(data):
        arr = []
        lhs, rhs = divide(data[:mid]), divide(data[mid:])

        while (lhs and rhs):

            if lhs[0] > rhs[0]:
                arr.append(rhs.pop(0))
            else:
                arr.append(lhs.pop(0))

        arr.extend((lhs + rhs))

        return arr
    else:
        return data


def merge(list1, list2):
    return divide(list1 + list2)


# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
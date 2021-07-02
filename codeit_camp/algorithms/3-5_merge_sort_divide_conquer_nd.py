def merge(list1, list2):
    result = []

    i = j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1
    result += list1[i:] + list2[j:]
    return result


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    lhs, rhs = merge_sort(my_list[:mid]), merge_sort(my_list[mid:])

    return merge(lhs, rhs)


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

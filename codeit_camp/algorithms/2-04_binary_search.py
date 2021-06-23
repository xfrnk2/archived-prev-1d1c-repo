#첫 try, while문 만 적어서는 실패하는 코드를 작성했음, 그래서 아래에 추가 조건식을 적어 채점에 통과하도록함. 그러나 지저분한 코드.

def binary_search(element, some_list):
    start, end = 0, len(some_list) - 1

    while start + 1 < end:
        pivot = (start + end) // 2
        if some_list[pivot] == element:
            return pivot
        elif some_list[pivot] > element:
            end = pivot
        elif some_list[pivot] < element:
            start = pivot

    if some_list[start] == element:
        return start
    elif some_list[end] == element:
        return end
    else:
        return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
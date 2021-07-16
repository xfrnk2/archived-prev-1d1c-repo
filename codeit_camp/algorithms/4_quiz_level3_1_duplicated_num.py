# 제약사항에 맞춰서 풀었는데 해설에서는 이진 탐색을 설명하고 있다. 차후 이진 탐색으로 풀어보길 바란다.

def find_same_number(some_list):
    some_list.sort()
    prev = some_list[0]
    for i in range(1, len(some_list)):
        if some_list[i] == prev:
            return some_list[i]
        prev = some_list[i]

# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))
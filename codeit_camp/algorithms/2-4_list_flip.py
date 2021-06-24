# 파라미터 some_list를 거꾸로 뒤집는 함수

def flip(some_list):
    if len(some_list) == 1:
        return some_list
    mid = len(some_list) // 2
    return flip(some_list[mid:]) + flip(some_list[:mid])


# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
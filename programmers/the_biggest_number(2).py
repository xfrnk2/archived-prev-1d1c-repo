from functools import cmp_to_key
# def ascending_order(x, y):
#     return int(y+x) - int(x+y)

def solution(numbers):
    answer = ''.join(sorted(map(str, numbers), key=cmp_to_key(lambda x, y:int(y+x)-int(x+y))))
    return answer if int(answer) else '0'


print(solution([6, 10, 12]))
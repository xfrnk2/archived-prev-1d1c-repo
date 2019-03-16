import copy

def solution(cryptogram):

    if not isinstance(cryptogram, str) or not 1 < len(cryptogram) <= 1000\
        or cryptogram.islower() is False:
        print("잘못된 입력입니다")
        exit()

    origin = list(cryptogram)
    result = list(cryptogram)
    limit = 0

    while len(origin) > len(set(origin)):
        for x in range(len(origin)):
            if x == 0:
                continue
            else:
                if origin[x] == origin[x-1]:
                    if len(origin) <= 7:
                        limit = x - 2

                    else:
                        limit = x - 3
                    a = origin[x]
                    value = result.index(a, limit)
                    result.pop(value)
                    result.pop(value)
        print(''.join(result))
        limit = 0
        origin = copy.deepcopy(result)
    answer = ''.join(result)
    return answer



cryptogram = "browoanoommnaon"
solution(cryptogram)

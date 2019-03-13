# https://python.bakyeono.net/chapter-9-4.html

import copy
#에러종류모음 : https://docs.python.org/ko/3/library/exceptions.html
class IsNotNumberError:
    pass

class DoublesignError:
    def __init__(self):
        print("에러메세지 : 연산자가 연속 입력되었습니다")


def check_str(x):  # x is str
    assert x or x is not str, "입력받은 식이 없거나 식이 문자열이 아닙니다"
    box = list(x)  # box is list
    sign = ['+', '-', '*', '/']
    sign_limit = 0

    try:

        for i in x:

            if i.isdigit():
                continue
            assert i in sign, "정수가 아니거나, 연산자가d 아닌 값이 입력되었습니다"

            # i의 인덱스
            value = box.index(i, sign_limit)
            # 연산자 연속 입력시 에러 발생
            if x[x.index(i) + 1] in sign:
                raise DoublesignError()
            # 연산자가 2개이상일때 탐색시작지점을 sign_limit으로 적용
            if x.count(i) >= 2:
                sign_limit = value + 3

            box.insert(value, ' ')
            box.insert(value + 2, ' ')

    except DoublesignError as e:
        print(e)

    finally:
        result = ''.join(box)
        result = result.split()
        return result


def get_priority_sign(expression): # list를 받아온다
    assert expression, "입력된 식이 없습니다"

    priority_sign = ['*', '/']
    priority_group = {}
    not_priority_group = {}

    try:

        for i in expression:

            index = expression.index(i)
            if i.isdigit():
                continue
            if i in priority_sign:
                priority_group[index] = i
            if not i in priority_sign:
                not_priority_group[index] = i

    except TypeError as e:
        print(e)

    except IndexError as e:
        print(e)

    except KeyError as e:
        print(e)

    return priority_group, not_priority_group


def calculating(expression, priority_sign, not_priority_sign):
    example = copy.deepcopy(expression)
 

    return example

def main():

    result = None
    try:
        expression = input("식을 입력하세요")
        assert expression != "", "입력된 식이 없습니다"

        result = check_str(expression)
        priority_sign, not_priority_sign = get_priority_sign(result)

        print(calculating(result, priority_sign, not_priority_sign))



    finally:
        print(result)


main()
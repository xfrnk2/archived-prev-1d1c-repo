# https://python.bakyeono.net/chapter-9-4.html


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
            assert i in sign, "정수가 아니거나, 연산자가 아닌 값이 입력되었습니다"

            # i의 인덱스
            value = box.index(i, sign_limit)

            if x[x.index(i) + 1] in sign:
                raise DoublesignError()

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
    sign = ['+', '-', '*', '/']
    priority_sign = ['*', '/']
    sign_index_group = {}

    for i in expression:
        if i in sign:
            sign_index_group[expression.index(i)] = i

    for index, signal in sign_index_group.items():
        if signal in priority_sign:
            sign_index_group.pop(index)





def main():

    result = None
    try:
        expression = input("식을 입력하세요")
        assert expression != "", "입력된 식이 없습니다"

        result = check_str(expression)
        get_priority_sign(result)

    finally:
        print(result)

main()
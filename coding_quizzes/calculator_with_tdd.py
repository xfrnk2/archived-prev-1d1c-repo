# https://python.bakyeono.net/chapter-9-4.html


#에러종류모음 : https://docs.python.org/ko/3/library/exceptions.html
class IsNotNumberError:
    pass


def check_str(x):
    value = x
    sign = ['+', '-', '*', '/']
    sign_limit = 0
    for i in x:

        if i.isdigit():
            continue
        assert i in sign, "정수가 아니거나, 연산자가 아닌 값이 입력되었습니다"
        # if i in sign:


    return value

def main():
    expression = None
    result = None
    try:
        expression = input("식을 입력하세요")
        assert expression != "", "입력된 식이 없습니다"

        result = check_str(expression)


    finally:
        print(result)

main()
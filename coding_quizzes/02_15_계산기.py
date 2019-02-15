# GUI로 조작과 입력이 가능한 계산기를 만들어보자. 괄호와 + , - , * , / 연산이 가능한 계산기 완성하기.
import copy

def add(expression):
    _expression = expression
    flag = True
    sign = None
    index = 0
    index_group = {}
    target = None

    while flag:

        value = 0

        if '*' in _expression:
            value = _expression.index('*')
            index_group[value] = '*'
        if '/' in _expression:
            value = _expression.index('/')
            index_group[value] = '/'
        if '+' in _expression:
            value = _expression.index('+')
            index_group[value] = '+'
        if '-' in _expression:
            value = _expression.index('-')
            index_group[value] = '-'

        to_test = copy.deepcopy(index_group)
        for key, signal in to_test.items():

            if signal == '+':
                if '*' in to_test.values():
                    index_group.pop(key)
                    continue
                if '/' in to_test.values():
                    index_group.pop(key)
                    continue
            if signal == '-':
                if '*' in index_group.values():
                    index_group.pop(key)
                    continue
                if '/' in index_group.values():
                    index_group.pop(key)
                    continue

        if index_group:
            target = min(index_group)

        else:
            break
        sign = index_group[target]
        index = _expression.index(sign)
#나눗셈에 의해 값이 소수점으로 떨어지게 되면 인덱스를 한 문자 단위로만 인식하기 때문에 올바른 계산이 되지 않는다.
        if sign == '+':
            value = int(_expression[index - 1]) + int(_expression[index + 1])
        if sign == '-':
            value = int(_expression[index - 1]) - int(_expression[index + 1])
        if sign == '*':
            value = int(_expression[index - 1]) * int(_expression[index + 1])
        if sign == '/':
            value = int(_expression[index - 1]) / int(_expression[index + 1])
            value = str(value)
            if '.' in value:
                float_test = value[value.find('.'):]
                if float_test.find('0') == -1:
                    print("정수가 아니잖아..")
                    exit()
                else:
                    location = value.find('.')
                    value = (value[0:location])

        _expression = _expression[:index - 1] + str(value) + _expression[
                                                             index + 2:]
        # assert value is int, f"나눗셈에 의한 결과값 {int(value)}이 정수가 아니여서 프로그램 종료"
        index_group = {}
        if _expression.isdigit():
            flag = False

    return _expression

# 나눗셈에 의해 정수가 아닌 값이 출현하는 예 -> 1+2/8*2-5 -> assert 에러 발생
print(add('1+8/2*2-5'))

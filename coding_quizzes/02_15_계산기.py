# GUI로 조작과 입력이 가능한 계산기를 만들어보자. 괄호와 + , - , * , / 연산이 가능한 계산기 완성하기.
import copy

def add(expression):
    _expression = copy.deepcopy(expression)
    _expression = list(_expression)
    flag = True
    flag0 = True
    sign = None
    index = 0
    index_group = {}
    target = None

    # 연산자 기호가 2개 이상일 경우 다시 찾을때 이미 찾은 값 다음의 인덱스부터 찾을수 있도록 제한두기위한 변수
    plus_limit = 0
    minus_limit = 0
    multi_limit = 0
    div_limit = 0

    for x in expression:

        if x.isdigit():
            continue

        if x == '+':

            value = _expression.index('+', plus_limit)
            if _expression.count('+') >= 2:
                plus_limit = value + 4
                #공백이 두개 늘어나기 때문에 value + 1이어서는 정확한 위치를 설정하기 어려우므로
                #value가 3 이상이어야 하는데 기호의 위치부터인 4를 더하기로 했다.

            _expression.insert(value, ' ')
            _expression.insert(value + 2, ' ')

            continue

        if x == '-':

            value = _expression.index('-', minus_limit)
            if _expression.count('-') >= 2:
                minus_limit = value + 4

            _expression.insert(value, ' ')
            _expression.insert(value + 2, ' ')
            continue

        if x == '*':

            value = _expression.index('*', plus_limit)
            if _expression.count('*') >= 2:
                multi_limit = value + 4

            _expression.insert(value, ' ')
            _expression.insert(value + 2, ' ')
            continue

        if x == '/':

            value = _expression.index('/', plus_limit)
            if _expression.count('/') >= 2:
                div_limit = value + 4

            _expression.insert(value, ' ')
            _expression.insert(value + 2, ' ')
            continue

    _expression = ''.join(_expression)
    _expression = _expression.split()
    # return _expression

    while flag:

        plus_limit = 0
        minus_limit = 0
        multi_limit = 0
        div_limit = 0
        value = 0
        for y in _expression:

            if y.isdigit():
                continue

            if '*' == y:
                value = _expression.index('*', multi_limit)
                if _expression.count('*') >= 2:
                    multi_limit = value + 2
                index_group[value] = '*'
                continue

            if '/' == y:
                value = _expression.index('/', div_limit)
                if _expression.count('/') >= 2:
                    div_limit = value + 2
                index_group[value] = '/'
                continue

            if '+' == y:
                value = _expression.index('+', plus_limit)
                if _expression.count('+') >= 2:
                    plus_limit = value + 2
                index_group[value] = '+'
                continue

            if '-' == y:
                value = _expression.index('-', minus_limit)
                if _expression.count('-') >= 2:
                    minus_limit = value + 2
                index_group[value] = '-'
                continue


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

        _expression = _expression[:index - 1] + [str(value)] + _expression[
                                                             index + 2:]
        # assert value is int, f"나눗셈에 의한 결과값 {int(value)}이 정수가 아니여서 프로그램 종료"
        index_group = {}
        if ''.join(_expression).isdigit():
            flag = False

    return _expression

# 나눗셈에 의해 정수가 아닌 값이 출현하는 예 -> 1+2/8*2-5 -> assert 에러 발생
print(add('1+8/2*2-50-1+7'))

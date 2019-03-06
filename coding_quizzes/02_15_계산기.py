# GUI로 조작과 입력이 가능한 계산기를 만들어보자. 괄호와 + , - , * , / 연산이 가능한 계산기 완성하기.
import copy
import tkinter
from tkinter import messagebox


# 연산자가 연속으로 입력되었을때 잘못된 계산식임을 알리고 작동을 중지시키기 위한 함수
def check_sign_overlap(group, index):
    if group[index + 1].isdigit() is False:
        print("연산자가 연달아 입력되었으니 계산을 종료합니다. 올바른 계산식을 입력해 주세요")
        exit()


def calculating(group, sign, index):
    value = 0
    if sign == '+':
        value = int(group[index - 1]) + int(group[index + 1])
    if sign == '-':
        value = int(group[index - 1]) - int(group[index + 1])
    if sign == '*':
        value = int(group[index - 1]) * int(group[index + 1])
    if sign == '/':
        value = int(group[index - 1]) / int(group[index + 1])
        value = str(value)

        if '.' in value:
            float_test = value[value.find('.'):]
            if float_test.find('0', -1) == -1:
                print("정수가 아니잖아..")
                exit()
            else:
                location = value.find('.')
                value = (value[0:location])

    _expression = group[:index - 1] + [str(value)] + group[
                                                     index + 2:]

    return _expression


def add_space(expression, _expression):
    sign = ['+', '-', '*', '/']
    sign_limit = [0, 0, 0, 0]
    number = None
    for x in expression:

        if x.isdigit():
            continue

        if x == '+':
            number = 0
        elif x == '-':
            number = 1
        elif x == '*':
            number = 2
        elif x == '/':
            number = 3

        value = _expression.index(sign[number], sign_limit[number])
        check_sign_overlap(_expression, value)
        if _expression.count(sign[number]) >= 2:
            sign_limit[number] = value + 4
            # 공백이 두개 늘어나기 때문에 value + 1이어서는 정확한 위치를 설정하기 어려우므로
            # value가 3 이상이어야 하는데 기호의 위치부터인 4를 더하기로 했다.

        _expression.insert(value, ' ')
        _expression.insert(value + 2, ' ')

    return _expression


def add(expression):
    _expression = copy.deepcopy(expression)
    _expression = list(_expression)
    # 연산자 기호가 2개 이상일 경우 다시 찾을때 이미 찾은 값 다음의 인덱스부터 찾을수 있도록 제한두기위한 변수

    # 문자열로된 식을 받아와서 연산자와 숫자 끼리 나눌 수 있도록 공백을 넣어주는 함수 add_space를 호출한다.
    _expression = add_space(expression, _expression)

    _expression = ''.join(_expression)
    _expression = _expression.split()

    flag = True
    index_group = {}
    #
    while flag:

        plus_limit = 0
        minus_limit = 0
        multi_limit = 0
        div_limit = 0

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

        _expression = calculating(_expression, sign, index)

        index_group = {}
        if ''.join(_expression).isdigit():
            flag = False

    return _expression


window = tkinter.Tk()
window.title("계산기")
window.geometry("640x400+100+100")
window.resizable(False, False)

lbl = tkinter.Label(window, text="식")
lbl.grid(row=0, column=0)
txt = tkinter.Entry(window)
txt.grid(row=0, column=1)


def call_back():
    total = txt.get()
    result = add(total)
    tkinter.messagebox.showinfo("결과값!", f"{result}입니다")


btn = tkinter.Button(window, text="OK", width=15, command=call_back)
btn.grid(row=1, column=1)

window.mainloop()

# 나눗셈에 의해 정수가 아닌 값이 출현하는 예 -> 1+2/8*2-5 -> 정수가 아니므로 실행 종료
print(add('1+8/2*2-50-1+7'))

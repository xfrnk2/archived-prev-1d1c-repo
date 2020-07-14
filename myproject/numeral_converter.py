import os

# 도움을 얻은 곳 : 리스트 컴프리헨션 구성을 위해 열람 : https://doorbw.tistory.com/174
# 진법 변환 내장함수 정보(블로그) : https://www.daleseo.com/python-int-bases/
'''
2진수: 0b
8진수: 0o
16진수: 0x
'''

def check_value(num, numSet):
    if int(numSet) in (2, 8, 10) and num.isdecimal():
        return not bool(list(filter(lambda x: int(numSet) - 1 < int(x), num)))
    elif numSet == '16':
        if num.isdecimal():
            return True
        else:
            return not list(filter(lambda n: n.isalpha() and n not in ['A', 'B', 'C', 'D', 'E', 'F'], num))
    return False

if __name__ == '__main__':
    result = ''
    getSet = outSet = number = ''
    numSet = {'2': ('0b','bin'), '8': ('0o','oct'), '10': ('','str'), '16': ('0x','hex')}

    print("n진수를 m진수로 바꾸는 변환 프로그램입니다")
    while True:
        getSet = input("입력값이 몇진법의 수인지 수의 값을 입력해 주세요(2, 8, 10, 16)\n입력 : ")
        if getSet.isdecimal() and getSet in numSet:
            break
        os.system('cls')
        print('(2, 8, 10, 16) 중 하나의 숫자로 정확한 값을 입력 해 주세요. \n다시 ', end='')

    while True:
        number = input(f"입력받을 값의 진수 : {getSet}\n해당 진법에 맞게 수를 입력하세요. \n입력 : ")
        if check_value(number, getSet):
            break
        print("해당 진법에서 허용하는 정확한 정수의 값을 입력하기 바랍니다.")
        os.system('cls')

    while True:
        outSet = input(f"입력받은 값의 진수 : {getSet} \n입력 받은 값 : {number}\n바꿀 진법수의 값을 입력해 주세요(2, 8, 10, 16)\n 입력 : ")
        if outSet.isdecimal() and outSet in numSet:
            break
        os.system('cls')
        print('(2, 8, 10, 16) 중 하나의 숫자로 정확한 값을 입력 해 주세요. \n다시 ', end='')



    introCom, convertCom = numSet[getSet][0], numSet[outSet][1]
    result = eval(convertCom + f'({introCom + number})')
    if not outSet == '10':
        result = result[2:]
    print('결과 : ', result, f'({outSet}진수)')

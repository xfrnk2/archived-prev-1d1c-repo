# 도움을 얻은 곳 : 리스트 컴프리헨션 구성을 위해 열람 : https://doorbw.tistory.com/174
import os
from functools import reduce
# 실수일때는 나중에(소수점 아래로 존재시)


def binaryToDecimal(num:str) -> int:
    result = 0
    for i,j in enumerate(num[::-1]):
        result += int(j)*(2**i)
    return result


def binaryToOctal(num: str) -> int:
    result = ''
    temp = ''
    for i, j in enumerate(num[::-1]):
       if j == '1':
            temp += str(2 **(i%3))

       if (i+1) % 3 == 0 or i == len(num)-1:
            result += str(reduce(lambda x, y: int(x) + int(y), temp))
            temp = ''
    return int(result[::-1])

def decimalToBinary(num):
    pass
def decimalToOctal(num):
    pass
def octalToBinary(num):
    pass
def octalToDecimal(num):
    pass


def checkValue(value: str, numSet: str) -> bool:
    if 2 <= int(numSet) <= 10:
        if not value.isdecimal():
            return False

        if numSet == '2':
            for n in value:
                if not 0 <= int(n) < 2:
                    return False
        elif numSet == '8':
            for n in value:
                if not 0 <= int(n) <= 8:
                    return False
        return True
    else:#16진수
        pass
            
    return True

if __name__ == '__main__':
    result = ''
    getSet = outSet = number = ''
    numSet = ['2', '8', '10', '16']
    hexDic = {
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }


    print("n진수를 m진수로 바꾸는 변환 프로그램입니다")
    while True:
        getSet = input("입력값이 몇진법의 수인지 수의 값을 입력해 주세요(2, 4, 8, 16)\n입력 : ")
        if getSet.isdecimal() and getSet in numSet:
            break
        os.system('cls')
        print('(2, 8, 10, 16) 중 하나의 숫자로 정확한 값을 입력 해 주세요. \n다시 ', end='')

    while True:
        number = input(f"입력받을 값의 진수 : {getSet}\n해당 진법에 맞게 수를 입력하세요. \n입력 : ")
        if checkValue(number, getSet):
            break
        print("해당 진법에서 허용하는 정확한 정수의 값을 입력하기 바랍니다.")
        os.system('cls')

    while True:
        outSet = input(f"입력받은 값의 진수 : {getSet} \n입력 받은 값 : {number}\n바꿀 진법수의 값을 입력해 주세요(2, 4, 8, 16)\n 입력 : ")
        if getSet.isdecimal() and getSet in numSet:
            break
        os.system('cls')
        print('(2, 8, 10, 16) 중 하나의 숫자로 정확한 값을 입력 해 주세요. \n다시 ', end='')

    if (getSet, outSet) == ('2', '8'):
        result = binaryToOctal(number)
    elif (getSet, outSet) == ('2', '10'):
        result = binaryToDecimal(number)
    elif (getSet, outSet) == ('8', '2'):
        result = octalToBinary(number)
    elif (getSet, outSet) == ('8', '10'):
        result = octalToDecimal(number)
    elif (getSet, outSet) == ('10', '2'):
        result = decimalToBinary(number)
    elif (getSet, outSet) == ('10', '8'):
        result = decimalToOctal(number)

    print("결과 : ", result)
    # conToDem = lambda x: int(x) if x.isdecimal() else dic[x]
    # get_input = [conToDem(n) for n in list(input())]

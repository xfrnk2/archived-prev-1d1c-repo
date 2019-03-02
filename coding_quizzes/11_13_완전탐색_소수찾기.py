"""
 https://programmers.co.kr/learn/courses/30/lessons/42839
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.



입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
11과 011은 같은 숫자로 취급합니다.


참고 사이트
https://programmers.co.kr/learn/courses/4008/lessons/12836
https://kkamikoon.tistory.com/90
"""
import random
import itertools


def get_numbers():
    numbers = ""
    numbers_length = random.randrange(3, 5)
    for _ in range(numbers_length):
        y = random.randrange(0, 10)
        y = str(y)
        numbers += y
    return numbers


def check_num(x, y):
    while True:
        if x < y:
            return False
        if y == x:
            return True
        if x % y == 0:
            return False
        else:
            y += 1


def simulate(val):
    numbers = val  # 무작위 길이의 무작위 숫자들을 숫자를 얻어온다
    numbers_len = len(numbers)  # 숫자의 길이

    print("얻어온 숫자의 값 : ", numbers)

    value2 = list(numbers)  # 리스트화 시킨다

    abc = []  # 만들수 있는 경우의 수들을 저장할 장소

    for i in range(1, numbers_len + 1):  # 만들 수 있는 모든 경우의 수를 abc에 추가한다
        value = list(map(''.join, itertools.permutations(value2, i)))
        abc.extend(value)

    print("만들수 있는 모든 경우의 수", abc)

    for x in range(len(abc)):  # 문자열 좌측의 0을 모두 삭제한다
        if '0' in abc[x]:
            abc[x] = abc[x].lstrip("0")

    print(abc)

    print("\n")
    abc.sort()  # 정렬시킨다
    abc = list(set(abc))
    abc.sort(key=len)  # 오름차순 정렬
    while '' in abc:  # 기존 값이 0이여서 값이''가 된  원소를 남아있지 않을 때까지 완전히 삭제시킨다
        abc.remove('')

    real = []  # 소수를 담아둘 장소

    for x in range(len(abc)):  # 소수가 맞는지 확인
        y = 2

        abc[x] = int(abc[x])
        result = check_num(abc[x], y)  # 소수 확인을 위한 함수 호출
        if result:
            real.append(abc[x])  # 소수이면 리스트에 저장

    real.sort()
    return real
    # print("haha", abc)
    #     for y in range(len(value)):
    #         abc.append(value[y])
    # abc = list(set(abc))
    # abc.sort(key=len)
    # print("haha",abc)
    #
    # for x in range(len(abc)):
    #
    #     if '0' in abc[x] :
    #         abc[x].lstrip("0")
    #     if abc[x] == '0':
    #         abc.pop(x)
    #
    # print(abc)

    # value = list(set(value))
    #
    # # for y in value:
    # #     if '0' in y:
    # #         if y[0] == '0':
    # #             y = y[:1]
    # #             # value.pop(value.index(y))
    # #
    # #             for i in range(numbers_len):
    # #                 if y[i] == '0':
    # #                     y = y[:i+1]
    # #                 else:
    # #                     break
    #
    # # results.append(list(map(''.join, itertools.permutations(value2, i))))
    # results.append(value)
    #
    # for y in results[i-1]:
    #     that = results[i - 1].index(y)
    #     if y == '0':
    #         print("hahaha",that)
    #         results[i-1].pop(that)
    #     y.lstrip("0")

    # i개의 갯수만큼의 원소로 수열 만들기
    # 1~ numbers_len의 길이만큼 갯수로..

    # for x in numbers:
    #     x = int(x)
    #
    #     if x == 2:
    #         results1 += str(2)
    #     elif x > 2:
    #         flag = True
    #         for y in range(2, x):
    #             if flag is False:
    #                 break
    #             if x % y == 0:
    #                 flag = False # false면 소수가 아닌거로 친다
    #         if flag:
    #             x = str(x)
    #             results1 += x
    #
    # print(results1)

    # for i in results1:
    #     print(i, " and ")


def main():
    result = simulate(get_numbers())

    if len(result) == 0:
        print("만들 수 있는 소수가 없습니다")
    else:
        print('만들수 있는 소수는..', result)


main()

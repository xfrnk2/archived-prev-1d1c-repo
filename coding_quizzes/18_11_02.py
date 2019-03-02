# https://programmers.co.kr/learn/courses/30/lessons/42748
"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
1.array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2.1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3.2에서 나온 배열의 3번째 숫자는 5입니다.

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
•array의 길이는 1 이상 100 이하입니다.
•array의 각 원소는 1 이상 100 이하입니다.
•commands의 길이는 1 이상 50 이하입니다.
•commands의 각 원소는 길이가 3입니다.

입출력 예

array

commands

return

[1, 5, 2, 6, 3, 7, 4] [[2, 5, 3], [4, 4, 1], [1, 7, 3]] [5, 6, 3]

입출력 예 설명

[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
 [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
 [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.


"""

import string


def solution(commands):
    assert 1 <= len(commands) <= 50, '매개변수 commands의 길이가 1~50의 범위를 벗어났습니다'
    _value = commands[0]
    i = commands[1][0]
    j = commands[1][1]
    k = commands[1][2]

    value1 = _value[i-1:j]
    print(value1)


    print(f"{_value}를 {i}번째부터 {j}번째까지 자른 후 정렬합니다")
    print(f"{value1}의 {k}번째 숫자는 {value1[k-1]} 입니다.")


def is_digit(num):

   try:
       int(num)
       return True
   except TypeError:
       return False

if __name__ == '__main__':
    commands = []
    array = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert 1 <= len(array) <= 100, '배열의 길이가 1~100의 범위를 벗어났습니다'
    print("배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.")
    print("숫자만 입력 가능합니다")
    while True:
        flag = True
        ijk = (input("i, j, k를 입력하세요. 띄어쓰기(공백)으로 구분합니다"))
        ijk = ijk.split()

        #정수로 바꿔준다
        for x in range(3):
            ijk[x] = int(ijk[x])


        if len(ijk) != 3:
            print("숫자 3개를 제대로 입력하세요")
            continue

        if ijk[1] - ijk[0] < ijk[2] :
            print("k의 입력이 올바르지 않습니다. k는 j에서 i를 뺀 수보다 같거나 작아야 합니다")
            continue




        else:

            commands.append(array)
            commands.append(ijk)
            solution(commands)
            break

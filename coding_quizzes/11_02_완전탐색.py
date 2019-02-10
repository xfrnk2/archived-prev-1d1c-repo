"""
https://programmers.co.kr/learn/courses/30/lessons/42840
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
•시험은 최대 10,000 문제로 구성되어있습니다.
•문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
•가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예 설명

입출력 예 #1
•수포자 1은 모든 문제를 맞혔습니다.
•수포자 2는 모든 문제를 틀렸습니다.
•수포자 3은 모든 문제를 틀렸습니다.

따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2
•수포자 1은 [1, 4]번 문제를 맞혔습니다.
•수포자 2는 다섯 번째 문제를 맞혔습니다.


일단 정답안은 최대 10000까지이다
랜덤인걸로 하고..
"""
import random


def _answers():
    array = []
    for _ in range(1, 1001):
        array.append(random.randrange(1, 6))
    return array


def person1():
    array = []
    i = 0
    for _ in range(1, 1001):
        i += 1
        array.append(i)
        if i % 5 == 0:
            i = 0

    return array


def person2():
    array = []
    i = 1
    for x in range(1, 1001):

        if not x % 2 == 0:
            array.append(2)
        else:
            array.append(i)
            i += 1

        if x % 10 == 0:
            i = 1

    return array


def person3():
    array = []
    count = [3, 1, 2, 4, 5]
    for _ in range(200):
        for x in range(5):
            array.append(count[x])
            array.append(count[x])
    return array


def solution(answers):
    answer = []
    return answer


# 단일 함수의 코드 복잡도가 너무 높습니다. 분리 해 보세요.
def main():
    _person1 = []
    _person2 = []
    _person3 = []

    for x in range(1000):

        if _answers()[x] == person1()[x]:
            _person1.append(x + 1)
        if _answers()[x] == person2()[x]:
            _person2.append(x + 1)
        if _answers()[x] == person3()[x]:
            _person3.append(x + 1)

        # 최종적으로 맞춘 개수

    print("수포자 1은", _person1, "번 문제를 맞췄습니다")
    print("수포자 2은", _person2, "번 문제를 맞췄습니다")
    print("수포자 3은", _person3, "번 문제를 맞췄습니다\n")

    print("가장 높은 점수를 받은 사람 순서로 출력합니다")
    a = len(_person1)
    b = len(_person2)
    c = len(_person3)
    group = [0, 0, 0]
    result = [0, 0, 0]
    if a > b:
        group[0] += 1
    if a > c:
        group[0] += 1
    if b > c:
        group[1] += 1
    if b > a:
        group[1] += 1

    if c > a:
        group[2] += 1
    if c > b:
        group[2] += 1

    if group[0] > group[1] and group[0] > group[2]:
        result[0] = 1
        if group[1] > group[2]:
            result[1] = 2
            result[2] = 3
        else:
            result[2] = 2
            result[1] = 3
    if group[1] > group[0] and group[1] > group[2]:
        result[0] = 2
        if group[0] > group[2]:
            result[1] = 1
            result[2] = 3
        else:
            result[2] = 1
            result[1] = 3
    if group[2] > group[0] and group[2] > group[1]:
        result[0] = 3
        if group[0] > group[1]:
            result[1] = 1
            result[2] = 2
        else:
            result[2] = 1
            result[1] = 2

    print(result)


main()

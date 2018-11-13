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

"""
import random


def get_numbers():
    numbers = ""
    numbers_length = random.randrange(1, 8)
    for _ in range(numbers_length):
        y = random.randrange(0, 10)
        y = str(y)
        numbers += y
    return numbers

def main():
    numbers = get_numbers()
    numbers_len = len(numbers)
    results1 = ""

    print(numbers)
    print(numbers_len)


    for x in numbers:
        x = int(x)

        if x == 2:
            results1 += str(2)
        elif x > 2:
            flag = True
            for y in range(2, x):
                if flag is False:
                    break
                if x % y == 0:
                    flag = False # false면 소수가 아닌거로 친다
            if flag:
                x = str(x)
                results1 += x


    for i in results1:
        print(i, " and ")


                    




main()
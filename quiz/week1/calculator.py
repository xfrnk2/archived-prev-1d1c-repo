import os
from raven import Client

# def calculator():
#     num1 = int()
#     flag = False
#
#     while True:
#         if flag is False:
#             a = int(input("숫자를 입력하세요"))
#             num1 = a
#             flag = True
#         else:
#             menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.초기화 6.나간다"))
#             if menu <= 4:
#                 num2 = int(input("숫자를 입력하세요"))
#                 if menu == 1:
#                     num1 += num2
#                     print(num1)
#                 elif menu == 2:
#                     num1 -= num2
#                     print(num1)
#                 elif menu == 3:
#                     num1 *= num2
#                     print(num1)
#                 elif menu == 4:
#                     num1 /= num2
#                     print(num1)
#             elif menu == 5:
#                 flag = False
#                 print("초기화 되었습니다")
#             elif menu == 6:
#                 print("계산기를 끕니다")
#                 break
#             elif menu > 5:
#                 input("잘못 입력하셨습니다, 다시 선택하세요")
#
#
# calculator()


def calculator():
    background = ["식.", "값.", "★"]
    back = ["식.", "값.", "★"]
    calc = ["+", "-", "*", "÷"]
    num1 = int()
    flag = False
    print("계산기가 실행되었습니다. 괄호 사용은 현재 미구현입니다")
    while True:
        os.system('cls')
        for x in range(3):
            print(background[x], end='\n')

        if flag is False:
            a = int(input("숫자를 입력하세요"))

            num1 = a
            background[0] += str(num1)
            background[1] += str(num1)
            flag = True
        else:
            menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.초기화 6.나간다"))
            assert menu is not int
            # menu의 값이 정수가 아닐 경우 에러 발생
            if menu <= 4:
                num2 = int(input("숫자를 입력하세요"))
                if menu == 1:
                    background[0] += calc[0]
                    background[0] += str(num2)
                    num1 += num2
                    background[1] = num1
                elif menu == 2:

                    background[0] += calc[1]
                    background[0] += str(num2)
                    num1 -= num2
                    background[1] = num1
                elif menu == 3:

                    background[0] += calc[2]
                    background[0] += str(num2)
                    num1 *= num2
                    background[1] = num1
                elif menu == 4:

                    background[0] += calc[3]
                    background[0] += str(num2)
                    num1 /= num2
                    background[1] = num1
            elif menu == 5:
                flag = False
                background = back
                print("초기화 되었습니다")
            elif menu == 6:
                print("계산기를 끕니다")
                break
            elif menu > 6:
                input("잘못 입력하셨습니다, 다시 선택하세요")


client = Client(
    'https://65d575d59e1748299f322af362a6b529'
    ':c4ba94596b824466a1a11631ec50623c@sentry.team504.co.kr//2')

if __name__ == '__main__':
    # noinspection PyBroadException

    try:
        calculator()
    except Exception:
        client.captureException()

# def calculator():
#     while True:
#         menu = int(input("원하는 계산은? 1. 더하기, 2. 빼기, 3. 곱하기, 4. 나누기, 5. 나가기"))
#         if menu <= 4:
#             num1 = int(input("첫번째 숫자"))
#             num2 = int(input("두번째 숫자"))
#             if menu == 1:
#                 result = num1 + num2
#                 print(result)
#             elif menu == 2:
#                 result = num1 - num2
#                 print(result)
#             elif menu == 3:
#                 result = num1 * num2
#                 print(result)
#             elif menu == 4:
#                 result = num1 / num2
#                 print(result)
#         elif menu == 5:
#             print("계산기를 끕니다")
#             break
#         else:
#             input("잘못 입력하셨습니다, 초기 메뉴로 돌아갑니다")
#
# calculator()
#
#

def calculator():
    value = int()
    value2 = False

    while True:
        if value2 is False:
            a = int(input("숫자를 입력하세요"))
            value = a
            value2 = True
        else:
            menu = int(input("1.더한다 2.뺀다 3.곱한다 4.나눈다 5.나간다"))
            if menu <= 4:
                num1 = int(input("숫자를 입력하세요"))
                if menu == 1:
                    value += num1
                    print(value)
                elif menu == 2:
                    value -= num1
                    print(value)
                elif menu == 3:
                    value *= num1
                    print(value)
                elif menu == 4:
                    value /= num1
                    print(value)
            elif menu == 5:
                print("계산기를 끕니다")
                break
            elif menu > 5:
                input("잘못 입력하셨습니다, 다시 선택하세요")


calculator()
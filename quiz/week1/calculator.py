def calculator():
    while True:
        menu = int(input("원하는 계산은?"))
        if menu <= 4:
            num1 = int(input("첫번째 숫자"))
            num2 = int(input("두번째 숫자"))
            if menu == 1:
                result = num1 + num2
                print(result)
            elif menu == 2:
                result = num1 - num2
                print(result)
            elif menu == 3:
                result = num1 * num2
                print(result)
            elif menu == 4:
                result = num1 / num2
                print(result)
        elif menu == 5:
            print("계산기를 끕니다")
            break
        else:
            input("잘못 입력하셨습니다, 초기 메뉴로 돌아갑니다")

calculator()




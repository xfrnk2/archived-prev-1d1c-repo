# -*- coding: utf-8 -*-
# 요구명세 link : https://github.com/TeamLab/introduction_to_python_TEAMLAB_MOOC/blob/5a9657ee91691e9e4cc09e6c041b81192ec668c8/lab_assignment/lab_7/lab_7.pdf
import random

you_win = 0


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)

def is_digit(user_input_number):
    # '''
    result = None
    try:
        int(user_input_number)
        result = True
    except ValueError:
        result = False
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # result = None

    # ==================================
    return result


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    result = None
    value = int(user_input_number)

    if (100 <= value) and (value < 1000):
        result = True
    else:
        result = False
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # ==================================
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    result = None

    b = str(three_digit)
    a = list(b)
    if a[0] == a[1]:
        result = True

    elif a[0] == a[2]:
        result = True
    elif a[1] == a[2]:
        result = True
    elif a[0] == a[1] == a[2]:
        result = True
    else:
        result = False

    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # Hint - Len과 Set을 써서 할 수 있음, 중복되는 값의 str 길이는 1 또는 2

    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    result = None
    if user_input_number:
        if is_digit(user_input_number) is False:
            result = False

        elif is_between_100_and_999(user_input_number) is False:
            result = False

        elif is_duplicated_number(user_input_number) is True:
            result = False
    else:
        result = True

    #     if 100 <= user_input_number and user_input_number < 1000:
    #
    #         b = str(user_input_number)
    #         a = list(b)
    #
    #         if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
    #             result = True
    #
    #         else:
    #             result = False
    #     else:
    #         result = False
    # else:
    #     result = False

    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    while True:
        value = int(get_random_number())
        b = str(value)
        a = list(b)

        if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
            result = value
        else:
            continue
        # Output:
        #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
        #     정수값으로 문자열이 아님
        # Examples:
        #   >>> import baseball_game as bg
        #   >>> bg.get_not_duplicated_three_digit_number()
        #   125
        #   >>> bg.get_not_duplicated_three_digit_number()
        #   634
        #   >>> bg.get_not_duplicated_three_digit_number()
        #   583
        #   >>> bg.get_not_duplicated_three_digit_number()
        #   381
        # '''
        # ===Modify codes below=============
        # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
        # get_random_number() 함수를 사용하여 random number 생성

        # ==================================
        return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # user_input_number = 558
    # random_number = 559

    a = str(random_number)
    value1 = list(a)

    b = str(user_input_number)
    value2 = list(b)

    x = 0
    y = 0

    for a in range(3):
        for b in range(3):

            if a == b:
                if value1[a] == value2[b]:
                    x += 1

            elif value1[a] == value2[b]:
                    y += 1
            else:
                pass

    result = [x, y]
    print(f"[strikes : {x}, ball : {y}]")
    return result
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # ==================================


def is_yes(one_more_input):
    if one_more_input.upper() == 'Y' or one_more_input.upper() == 'YES':
        result = True
    else:
        result = False

    return result
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # ==================================


def is_no(one_more_input):
    if one_more_input.upper() == 'N' or one_more_input.upper() == 'NO':
        result = True
    else:
        result = False

    return result
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # ==================================


def main():
    flag = True
    print("Play Baseball")
    while flag is True:
        you_win = False
        random_number = get_not_duplicated_three_digit_number()
        print("Random Number is : ", str(random_number))
        user_input_number = input("please input your number")

        if is_validated_number(user_input_number) is False:
            print("Wrong Input, Input Again")
            continue
        else:
            result = (get_strikes_or_ball(user_input_number, random_number))

            while result == [3, 0]:

                retry = input("you win, one more(Y/N) ?")
                if is_yes(retry):
                    break
                elif is_no(retry):
                    print(
                        "Thank you for using this program\nEnd of the Game")
                    flag = False
                    break
                else:
                    print("Wrong Input, Input Again")
                    continue






# ===Modify codes below=============
# 위의 코드를 포함하여 자유로운 수정이 가능함


# menu = input("What would you want to do? \n 1. 2. 3. 4. 5.")
#
# if menu is '1':
#     a = is_digit(user_input_number)
#     print(a)
# elif menu is '2':
#     b = is_between_100_and_999(user_input_number)
#     print(b)
# elif menu is '3':
#     c = is_duplicated_number(user_input_number)
#     print(c)
# elif menu is '4':
#     d = is_validated_number(user_input_number)
#     print(d)
# elif menu is '5':
#     print(get_not_duplicated_three_digit_number())
# elif menu is '6':
#     ran = get_random_number()
#     print(get_strikes_or_ball(user_input_number, ran))
#     print(ran)


# ==================================
print("Thank you for using this program")
print("End of the Game")

if __name__ == "__main__":
    main()

'''
여기있는 모든 함수를 활용해서 주석처리된 내용에 맞게 코드작성하기
'''

# https://python.bakyeono.net/chapter-9-4.html
import unittest
#에러종류모음 : https://docs.python.org/ko/3/library/exceptions.html
class IsNotNumberError:
    pass

class DoublesignError:
    def __init__(self):
        print("에러메세지 : 연산자가 연속 입력되었습니다")


class Calcuator(unittest.TestCase):
    def check_str(self, x):  # x is str
        box = list(x)  # box is list
        sign = ['+', '-', '*', '/']
        sign_limit = 0

        try:

            for i in x:

                if i.isdigit():
                    continue

                # i의 인덱스
                value = box.index(i, sign_limit)
                # 연산자 연속 입력시 에러 발생
                if x[x.index(i) + 1] in sign:
                    raise DoublesignError()
                # 연산자가 2개이상일때 탐색시작지점을 sign_limit으로 적용
                if x.count(i) >= 2:
                    sign_limit = value + 3

                box.insert(value, ' ')
                box.insert(value + 2, ' ')

        except:
            print("정수가 아니거나, 연산자가 아닌 값이 입력되었습니다")


        finally:
            result = ''.join(box)
            result = result.split()
            return result

    def get_priority_sign(self, expression):  # list를 받아온다

        priority_sign = ['*', '/']
        priority_group = {}
        not_priority_group = {}

        try:

            for index, i in enumerate(expression):

                if i.isdigit():
                    continue
                if i in priority_sign:
                    priority_group[index] = i
                if not i in priority_sign:
                    not_priority_group[index] = i

        except Exception as e:
            print(e)
        return priority_group, not_priority_group

    def calculating(self, expression, priority_sign, not_priority_sign):
        limit = 0
        try:
            # 우선순위 기호(*,/)그룹인 priority_sign을 순회한다. index가 가장 작은 것부터 계산한다.
            for v in range(len(priority_sign)):
                minimum_value = min(priority_sign)
                minimum_index = priority_sign[minimum_value]
                value = expression.index(minimum_index, limit)

                if minimum_index == '*':
                    expression[value - 1] = int(expression[value - 1]) * int(
                        expression[value + 1])
                if minimum_index == '/':
                    expression[value - 1] = int(expression[value - 1]) / int(
                        expression[value + 1])

                limit = value - 1

                expression.pop(value), expression.pop(value)

            # 비우선순위 기호 순회
            for v in range(len(not_priority_sign)):
                minimum_value = min(not_priority_sign)
                minimum_index = not_priority_sign[minimum_value]
                value = expression.index(minimum_index, limit)

                if minimum_index == '+':
                    expression[value - 1] = int(expression[value - 1]) + int(
                        expression[value + 1])
                if minimum_index == '-':
                    expression[value - 1] = int(expression[value - 1]) - int(
                        expression[value + 1])

                limit = value - 1

                expression.pop(value), expression.pop(value)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            print(expression)

    def main(self):

        result = 0
        try:
            expression = input("식을 입력하세요")
            assert expression != "", AssertionError
        except AssertionError:
            print("식이 입력되지 않았습니다")

        except Exception as e:
            print(e)
        else:

            result = self.check_str(expression)
            priority_sign, not_priority_sign = self.get_priority_sign(result)

            result = self.calculating(result, priority_sign, not_priority_sign)

        finally:
           print(result)


if __name__ == '__main__':
    # unittest.main()
    cal = Calcuator()
    cal.main()


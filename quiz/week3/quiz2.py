"""
스택입니다(후입 선출의 자료구조)

아래의 TODO 항목을 읽어주세요.
"""

from quiz.week3.custm_list import List



class Stack:
    def __init__(self):
        self.__list = List()
        # 실험 적용 self.__size = 0


    def push(self, value) -> None:
        """
        값을 넣는다.
        :param value: 저장하려는 값
        :return:None
        """
        # TODO - 채워주세요
        self.__list.append(value)

    def pop(self) -> 'data':
        """
        가장 최근에 넣은 값을 꺼낸다.
        :return: 가장 최근에 넣은 값
        """
        # TODO - 채워주세요
        return self.__list.pop(self.size - 1)





        #self.__list.pop(self.__size - 1)


    def print(self):
        self.__list.print()

    @property
    def size(self):
        return self.__list.size


if __name__ == '__main__':
    custom_stack = Stack()

    custom_stack.push(1)
    custom_stack.push(2)
    custom_stack.print()

    assert custom_stack.size == 2, "Stack.push() 함수를 정확하게 구현하지 않았습니다"

    test_value1 = custom_stack.pop()
    assert custom_stack.size == 1, "Stack.pop() 함수를 정확하게 구현하지 않았습니다"

    test_value2 = custom_stack.pop()
    assert custom_stack.size == 0, "Stack.pop() 함수를 정확하게 구현하지 않았습니다"

    assert test_value1 == 2 and test_value2 == 1, \
        "Stack.pop() 함수를 정확하게 구현하지 않았습니다"

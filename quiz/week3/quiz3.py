# coding=utf-8

"""
큐입니다(선입 선출의 자료구조)

아래의 TODO 항목을 읽어주세요.
"""

from quiz.week3.custm_list import List
from quiz.week3.custm_list import Node


class Queue:
    def __init__(self):
        self.__list = List()

    def enqueue(self, value) -> None:
        """
        값을 넣는다.
        :param value: 저장하려는 값
        :return:None
        """
        # TODO - 채워주세요
        enqueue_node = self.__list.append
        if value:
            enqueue_node(value)

    #        target_node = self.__list.index(0)
    #
    #
    #        if target_node == 0:
    #            prev = self.__node
    #        else:
    #            prev = self.__list.get_node_at(target_node + 1)
    #        kijyun = self.__list.get_node_at(target_node)#
    #
    #        if kijyun.next_node:
    #            prev.next_node = kijyun.next_node
    #        target_node.next_node = Node(value)
    #        self.__size += 1

    def dequeue(self) -> 'data':
        """
        가장 먼저 넣은 값을 꺼낸다.
        :return: 가장 오래 전에 넣은 값
        """
        # TODO - 채워주세요
        return self.__list.pop(0)


    def print(self):
        self.__list.print()


    @property
    def size(self):
        return self.__list.size()


if __name__ == '__main__':
    custom_queue = Queue()

    custom_queue.enqueue(1)
    custom_queue.enqueue(2)
    custom_queue.print()

    assert custom_queue.size == 2, "Queue.push() 함수를 정확하게 구현하지 않았습니다"

    test_value1 = custom_queue.dequeue()
    assert custom_queue.size == 1, "Queue.pop() 함수를 정확하게 구현하지 않았습니다"

    test_value2 = custom_queue.dequeue()
    assert custom_queue.size == 0, "Queue.pop() 함수를 정확하게 구현하지 않았습니다"

    assert test_value1 == 1 and test_value2 == 2, \
        "Queue.pop() 함수를 정확하게 구현하지 않았습니다"

"""
단방향 링크드 리스트입니다.

아래의 TODO 항목을 읽어주세요.
"""

from week3.custm_list import Node


class List:
    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def append(self, value):
        last_node = self.__head.get_last_node()

        last_node.next_node = Node(value)
        self.__size += 1

    def index(self, idx) -> 'object':
        return self.__get_node_at(idx).data

    def insert(self, idx, value) -> None:
# 지정된 위치 idx에 값 value를 삽입한다
# 집주소
        if idx == 0:
            prev_node = self.__head
        else:
            prev_node = self.__get_node_at(idx-1)

        try:
            current_node = self.__get_node_at(idx)
        except IndexError:
            current_node = None

        new_node = Node(value)
        prev_node.next_node = new_node
        new_node.next_node = current_node


#        target_node = self.__get_node_at(idx)
#        to_replace_node = self.__get_node_at(idx+1)
#        henkou_node = self.__get_node_at(idx-1)
#        if to_replace_node :
#            target_node.next_node = to_replace_node.next_node#


#        self.__size += 1
#        henkou_node.next_node = Node(value)

         # 꼭 이 return이 있어야 할까..? 그렇다면 어떻게 써야 할까? 아직 잘 모르겠다.


  #      idx 번째에 해당 값을 저장하는 node 를 삽입합니다.
#
 #       :param idx: 몇번째에 해당하는 숫자(인덱스)
  #      :param value: 저장할 값
   #     :return: None
    #    """

        # TODO - 여기를 직접 구현해서 채워주세요

    def pop(self, idx=None) -> 'data':
        if idx == 0:
            prev = self.__head
        else:
            prev = self.__get_node_at(idx - 1)
        target = self.__get_node_at(idx)

        if target.next_node:
            prev.next_node = target.next_node

        self.__size -= 1
        return target.data

    def print(self):
        node = self.__head.next_node
        if node:
            print(node.get_all_data())

    @property
    def size(self):
        return self.__size

    def __get_node_at(self, idx):
        assert isinstance(idx, int)

        if idx < 0:
            raise IndexError

        if idx > self.__size - 1:
            raise IndexError

        node = self.__head
        for _ in range(idx + 1):
            node = node.next_node

        return node


if __name__ == '__main__':
    custom_list = List()

    custom_list.print()
    custom_list.append(2)
    custom_list.append(3)
    custom_list.append(5)
    custom_list.append(7)
    custom_list.print()

    # Index Error 발생
    # print(cl.index(4))

    for i in range(custom_list.size):
        print(f'index : {i}, data : {custom_list.index(i)}')

    print(custom_list.pop(2))
    custom_list.print()

    print(custom_list.pop(1))
    custom_list.print()

    custom_list.append('abc')
    custom_list.append('test')

    print(custom_list.pop(0))
    custom_list.print()

    test_data = 'hello'
    custom_list.insert(2, test_data)
    custom_list.print()

    result_data = custom_list.pop(2)

    # NOTE - 위의 TODO 항목을 정상적으로 정상적으로 구현하지 않으면 아래에서 오류가 발생합니다.
    assert test_data == result_data, "CustomList.insert() 함수를 정확하게 구현하지 않았습니다"

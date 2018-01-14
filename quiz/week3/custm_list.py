# coding=utf-8


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node: Node = None

    def get_all_data(self):
        result = f'[{str(self.data)}]'
        if self.next_node:
            result += f'-{self.next_node.get_all_data()}'

        return result

    def get_last_node(self):
        if self.next_node:
            return self.next_node.get_last_node()

        return self


class List:
    def __init__(self):
        self.__head = Node()
        self.head = Node()  # 실험 적용
        self.__size = 0

    def append(self, value):
        last_node = self.__head.get_last_node()

        last_node.next_node = Node(value)
        self.__size += 1

    def index(self, idx) -> 'object':
        return self.__get_node_at(idx).data

    def pop(self, idx=None) -> 'object':
        if idx == 0:
            prev = self.__head
        else:
            prev = self.__get_node_at(idx - 1)

        current = self.__get_node_at(idx)
        next_node = current.next_node

        if next_node:
            prev.next_node = next_node

        self.__size -= 1
        return current.data

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

    def get_node_at(self, idx):  # 실험 적용
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

    print(custom_list.size)
    custom_list.print()

    # Index Error 발생
    # print(cl.index(4))

    for i in range(custom_list.size):
        print(f'index : {i}, data : {custom_list.index(i)}')

    print(custom_list.pop(2))
    custom_list.print()

    print(custom_list.pop(1))
    custom_list.print()

    custom_list.append(6)
    custom_list.append(9)

    print(custom_list.pop(0))
    custom_list.print()

# coding=utf-8

"""
숫자를 받아들이는 이진 탐색 트리입니다.

아래의 TODO 항목을 읽어주세요.
"""


class Node:
    def __init__(self, data: int = None):
        self.__data: int = data
        self.__left_node: Node = None
        self.__right_node: Node = None

    def add_child(self, data: int = None) -> None:
        """
        자신보다 작은 값은 자신의 왼쪽 노드에,
        자신보다 큰 값은 자신의 오른쪽 노드에 추가합니다.

        이미 존재하는 값은 무시합니다.
        :param data: int
        :return: None
        """

    def find(self, data: int) -> bool:
        """
        자신 또는 자식에게 해당 값이 존재하는지 탐색합니다.
        있으면 True / 없으면 False 를 반환합니다.
        :param data: int
        :return: bool
        """

    def print_pre_order(self) -> None:
        """
        TODO - 전위 순회로 출력합니다.
        자신 -> 왼쪽 -> 오른쪽 순서대로 출력하면 됩니다.

        자신이 맨 앞(前)에 위치(位置)하므로 이므로 전위(前位)순회 입니다.

        :return: None
        """

    def print_in_order(self) -> None:
        """
        TODO - 중위 순회로 출력합니다.
        왼쪽 -> 자신 -> 오른쪽 순서대로 출력하면 됩니다.

        자신이 중간(中間)에 위치(位置)하므로 이므로 중위(中位)순회 입니다.

        :return: None
        """

    def print_post_order(self) -> None:
        """
        TODO - 후위 순회로 출력합니다.
        왼쪽 -> 오른쪽 -> 자신 순서대로 출력하면 됩니다.

        자신이 뒤(後)에 위치(位置)하므로 이므로 후위(後位)순회 입니다.

        :return: None
        """


class Tree:
    def __init__(self):
        self.__top = None

    def push(self, data) -> None:
        """
        TODO - 함수를 구현해 주세요.

        데이터를 입력 받아 적당한 하위 노드에 추가합니다.
        중복 입력은 무시합니다.
        :param data: int
        :return: None
        """

    def find(self, data) -> bool:
        """
        TODO - 함수를 구현해 주세요.

        트리 내부에 해당 값이 존재하는지 탐색합니다.
        :param data: int
        :return: bool
        """

    def print_pre_order(self) -> None:
        """
        TODO - 전위 순회로 출력합니다. Node 주석 참고
        :return: None
        """

    def print_in_order(self) -> None:
        """
        TODO - 중위 순회로 출력합니다. Node 주석 참고
        :return: None
        """

    def print_post_order(self) -> None:
        """
        TODO - 후위 순회로 출력합니다. Node 주석 참고
        :return: None
        """


if __name__ == '__main__':
    tree = Tree()

    #              5
    #            /   \
    #           3     7
    #          / \   / \
    #         2   4 6   9
    #        /         / \
    #       1         8  10

    tree.push(5)
    tree.push(3)
    tree.push(3)
    tree.push(7)
    tree.push(2)
    tree.push(6)
    tree.push(4)
    tree.push(4)
    tree.push(9)
    tree.push(8)
    tree.push(1)
    tree.push(10)

    assert tree.find(10) is True, "Tree.push()의 구현이 올바르지 않습니다."
    assert tree.find(2) is True, "Tree.push()의 구현이 올바르지 않습니다."
    assert tree.find(0) is False, "Tree.push()의 구현이 올바르지 않습니다."
    assert tree.find(12) is False, "Tree.push()의 구현이 올바르지 않습니다."

    # TODO - 아래의 함수는 이 순서대로 출력해야 합니다.

    # 5 3 2 1 4 7 6 9 8 10
    tree.print_pre_order()

    # 1 2 3 4 5 6 7 8 9 10
    tree.print_in_order()

    # 1 2 4 3 6 8 10 9 7 5
    tree.print_post_order()
# https://www.acmicpc.net/problem/10828
# 첫번재 풀이. 성공.
# from collections import deque
# import sys
# class Stack:
#     def __init__(self):
#         self.__data = deque()
#
#     def push(self, x):
#         self.__data.append(x)
#     def pop(self):
#         if not self.__data:
#             return print(-1)
#         print(self.__data.pop())
#     def size(self):
#         print(len(self.__data))
#     def empty(self):
#         print(int(bool(not self.__data)))
#
#     def top(self):
#         if not self.__data:
#             return print(-1)
#         print(self.__data[-1])
# stack = Stack()
#
# N = int(input())
# op = [sys.stdin.readline().split() for _ in range(N)]
#
# for x in op:
#     if x[0] == "push":
#         stack.push(int(x[1]))
#     elif x[0] == "pop":
#         stack.pop()
#     elif x[0] == "top":
#         stack.top()
#     elif x[0] == "size":
#         stack.size()
#     elif x[0] == "empty":
#         stack.empty()


# 두번째 풀이. 링크드 리스트//노드로 구현해보자.

import sys

class Stack:
    class Node:
        def __init__(self, num, link):
            self.num = num
            self.next = link
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        node = self.Node(x, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        if self.size <= 0:
            return print(-1)

        node = self.head
        self.head = node.next
        self.size -= 1
        print(node.num)

    def empty(self):
        if self.size == 0:
            return print(1)
        else:
            print(0)

    def top(self):
        if self.size == 0:
            return print(-1)

        print(self.head.num)

    def get_size(self):
        print(self.size)

stack = Stack()
for _ in range(int(sys.stdin.readline().rstrip())):
   order = sys.stdin.readline().rstrip()
   if 5 < len(order):
       stack.push(order[5:])
   elif order == "pop":
       stack.pop()
   elif order == "empty":
       stack.empty()
   elif order == "size":
       stack.get_size()
   elif order == "top":
       stack.top() #



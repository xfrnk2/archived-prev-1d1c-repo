# coding=utf-8


import copy
from event import Event
from game_object import GameObject


class Block(GameObject):
    def __init__(self):
        self.__data = '□'

    def __repr__(self):
        return self.__data

    def __str__(self):
        return self.__data

    def update(self, event: Event):
        pass

    def render(self):
        pass


class Field(GameObject):
    def __init__(self, width=25, height=30):
        self.__height = height
        self.__width = width
        self.__background = [[Block() for _ in range(width)] for _ in range(height)]
        self.__render_target = None

    def update(self, event: Event):
        self.__render_target = copy.deepcopy(self.__background)

    def render(self):
        for line in self.__render_target:
            output = ''
            for block in line:
                output += str(block)

            print(output)

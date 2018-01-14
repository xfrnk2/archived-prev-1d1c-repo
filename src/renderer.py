# coding=utf-8

import os

from field import Field

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        os.system('clear')


class Renderer:
    @staticmethod
    def init():
        pass

    @staticmethod
    def render_begin(field: Field):
        __class__.__field = field
        clear()

    @staticmethod
    def render_end():
        __class__.__field.render()
        pass

    @staticmethod
    def render(data, x, y):
        __class__.__field.set_render_data(data, x, y)

    @staticmethod
    def set_color(color):
        pass

    @staticmethod
    def set_bg_color(color):
        pass

    __field = None
    __screen = None
    __color = None
    __bg_color = None

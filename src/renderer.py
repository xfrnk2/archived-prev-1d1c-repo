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
        __class__.__fps = 0

    @staticmethod
    def render_begin(field: Field):
        __class__.__field = field
        # __class__.__fps += 1
        clear()

    @staticmethod
    def render_end():
        __class__.__field.render()
        print(f"FPS : {__class__.__fps}")
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
    __fps = 0

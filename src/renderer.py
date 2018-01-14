# coding=utf-8

import os

# Windows
if os.name == 'nt':
    def clear():
        """
        주석을 달아봅니다. cls 명령어를 실행해 출력화면을 백지 상태로 만듭니다
        """
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        """
        주석을 달아봅니다. cls 명령어를 실행해 출력화면을 백지 상태로 만듭니다
        """
        os.system('clear')


class Renderer:
    @staticmethod
    def init():
        pass

    @staticmethod
    def render_begin():
        clear()

    @staticmethod
    def render_end():
        pass

    @staticmethod
    def render(data, x, y):
        pass

    @staticmethod
    def set_color(color):
        pass

    @staticmethod
    def set_bg_color(color):
        pass

    __screen = None
    __color = None
    __bg_color = None

# coding=utf-8


from game_object import GameObject
from event import Event
from renderer import Renderer
from timer import Timer


class Puyo(GameObject):
    def __init__(self):
        self.__x = 12
        self.__y = 30
        self.__data = '⦿'

        self.__speed = 1

    def update(self, event: Event):
        self.__y -= self.__speed * Timer.get_elapsed()
        self.__y = max(self.__y, 0)

    def render(self):
        Renderer.render(self.__data, int(self.__x), int(self.__y))

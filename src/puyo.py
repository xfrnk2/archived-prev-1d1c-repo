# coding=utf-8


from game_object import GameObject
from event import Event
from renderer import Renderer
from timer import Timer


# noinspection SpellCheckingInspection
class Puyo(GameObject):
    def __init__(self):
        self.__x = 6
        self.__y = 20
        self.__data = '⦿'

        self.__speed = 1
        self.__alive = True
        self.__visible = True

    def update(self, event: Event):
        if self.__alive:
            self.__y -= self.__speed * Timer.get_elapsed()
            self.__y = max(self.__y, 0)

            if int(self.__y) == 0:
                self.die()

    def render(self):
        if self.__visible:
            Renderer.render(self.__data, int(self.__x), int(self.__y))

    def die(self):
        self.__alive = False

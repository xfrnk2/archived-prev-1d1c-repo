# coding=utf-8


from timer import Timer

from renderer import Renderer
from input import InputManager

from field import Field
from event import Event


class Game:
    def __init__(self):
        Timer.init()
        self.__input = InputManager()
        self.__game_objects = {}

    def init(self):
        self.__game_objects['field'] = Field()

    def run(self):
        is_continue = True
        while is_continue:
            is_continue = self.__update()
            self.__render()

    def close(self):
        self.__input.set_normal_term()

    def __update(self) -> bool:
        Timer.capture_time()

        escape = False

        input_manager = self.__input
        if input_manager.is_pressed():
            c = input_manager.get_key()
            if ord(c) == 27:  # ESC
                escape = True

        event = Event()

        for game_object in self.__game_objects.values():
            game_object.update(event)

        return not escape

    def __render(self):
        Renderer.render_begin()
        for game_object in self.__game_objects.values():
            game_object.render()
        Renderer.render_end()

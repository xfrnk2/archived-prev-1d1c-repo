# coding=utf-8


from timer import Timer

from renderer import Renderer
from input import InputManager

from field import Field
from event import Event

from puyo import Puyo


class Game:
    def __init__(self):
        Timer.init()
        Renderer.init()
        self.__input = InputManager()
        self.__game_objects = {}
        self.__field = Field()
        self.__accumulated_elapsed_render_time = Timer.get_elapsed()

        # 테스트용 임시 코드
        self.__game_objects['test_block'] = Puyo()

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

        self.__field.update(event)

        for game_object in self.__game_objects.values():
            game_object.update(event)

        return not escape

    def __render(self):
        self.__accumulated_elapsed_render_time += Timer.get_elapsed()

        # 5FPS(1초에 5번) 화면에 그리기 위해서
        if self.__accumulated_elapsed_render_time < 0.2:
            return

        self.__accumulated_elapsed_render_time = 0.0

        Renderer.render_begin(self.__field)
        for game_object in self.__game_objects.values():
            game_object.render()
        Renderer.render_end()

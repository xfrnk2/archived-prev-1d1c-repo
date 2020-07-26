from time import time
import os

class Timer:


    @staticmethod
    def init():
        __class__.prev_time = time()


    @staticmethod
    def capture_time():
        prev_time = __class__.prev_time
        current_time = time()
        __class__.elapsed_time = current_time - prev_time
        __class__.prev_time = current_time

    @staticmethod
    def get_elapsed():
        return __class__.elapsed_time

    prev_time = 0.0
    elapsed_time = 0.0

class Renderer:
    @staticmethod
    def init():
        __class__.__fps_count = 0
        __class__.__fps = 0
        __class__.__accumulated_elapsed_render_time = Timer.get_elapsed()
        __class__.__prev_tick = 0.0

    @staticmethod
    def render_begin() -> bool:
        elapsed_time = Timer.get_elapsed()
        __class__.__accumulated_elapsed_render_time += elapsed_time
        __class__.__prev_tick += elapsed_time

        # 5FPS(1초에 5번) 화면에 그리기 위해서
        if __class__.__accumulated_elapsed_render_time < 0.5:
            return False


        __class__.__accumulated_elapsed_render_time = 0.0
        __class__.__fps_count += 1

        if __class__.__prev_tick > 1.0:
            __class__.__fps, __class__.__fps_count = __class__.__fps_count, 0
            __class__.__prev_tick -= 1.0

        os.system('cls')

        return True

    @staticmethod
    def render_end():
        print(f"FPS : {__class__.__fps}")

    __fps_count = 0
    __fps = 0
    __accumulated_elapsed_render_time = 0.0
    __prev_tick = 0.0


class Game:
    def __init__(self):
        """

        :rtype:
        """
        Timer.init()
        Renderer.init()

    def run(self):

        is_continue = True
        while is_continue:
            is_continue = self.__update()
            self.__render()

    def __update(self) -> bool:

        Timer.capture_time()
        return True

    def __render(self):
        if not Renderer.render_begin():
            return

        Renderer.render_end()

game = Game()
game.run()
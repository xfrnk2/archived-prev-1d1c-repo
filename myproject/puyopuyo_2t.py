from time import time

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
        __class__.__accumulated_elapsed_render_time = Timer.get_elapsed()
    @staticmethod
    def ren():
        elapsed_time = Timer.get_elapsed()
        __class__.__accumulated_elapsed_render_time += elapsed_time
        print(__class__.__accumulated_elapsed_render_time)

        if __class__.__accumulated_elapsed_render_time > 0.2:
            print("over")
            return False


    __accumulated_elapsed_render_time = 0.0


Timer.init()
Renderer.init()
while True:
    Timer.capture_time()
    Renderer.ren()
    if not Renderer.ren():
        break
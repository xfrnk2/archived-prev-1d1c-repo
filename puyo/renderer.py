from mytimer import Timer
from field import PrintField
import os

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')


class renderer:

    __tick = 0
    __fps = 0.0
    __fps_count = 0.0
    __accumulated_elapsed_render_time = 0.0

    @staticmethod
    def init():
        __class__.__tick = 0
        __class__.__fps = 0.0
        __class__.__fps_count = 0.0
        __class__.__accumulated_elapsed_render_time = 0.0

    def render_begin(field:PrintField) -> bool:
        elapsed_time = Timer.get_elapsed_time()
        __class__.__accumulated_elapsed_render_time += elapsed_time
        __class__.__tick += elapsed_time

        if elapsed_time < 0.2:
            return False

        __class__.__field = field
        __class__.__accumulated_elapsed_render_time = 0.0
        __class__.__fps_count += 1

        if elapsed_time > 1.0:
            __class__.fps = __class__.__fps_count
            __class__.__fps_count = 0

            __class__.__tick -= 1.0

        clear()

        return True

    @staticmethod
    def render_end():
        __class__.__field.render()
        print(f"FPS : {__class__.__fps}")

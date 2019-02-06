import os
from time import time

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        os.system('clear')


class block():

    def __init__(self):
        self.__data = "□"

    def __str__(self):
        return self.__data

    def __repr__(self):
        return self.__data


class field():

    def __init__(self):
        self.__block = block()
        self.__field = [[self.__block for _ in range(6)] for _ in range(10)]

    def __str__(self):
        return self.__field

    def __repr__(self):
        return self.__field

    def print_field(self):
        print(self.__field)


class timer:
    prev_time = 0.0
    elapsed_time = 0.0


    @staticmethod
    def init():
        __class__.prev_time = time()
        __class__.elapsed_time = 0.0

    @staticmethod
    def get_elapsed_time():
        return __class__.elapsed_time

    @staticmethod
    def get_prev_time():
        return __class__.prev_time

    @staticmethod
    def reset_elapsed_time():
        __class__.elapsed_time = 0.0

    @staticmethod
    def reset_prev_time():
        __class__.prev_time = 0.0

    @staticmethod
    def capture():
        prev_time = __class__.prev_time
        current_time = time()
        __class__.elapsed_time += (current_time - prev_time)
        __class__.prev_time = current_time


class renderer():

    def __init__(self):
        self.__fps_count = 0

    def render_begin(self) -> bool:
        timer.capture()

        elapsed_time = timer.get_elapsed_time()
        if elapsed_time < 0.2:
            return False

        if elapsed_time > 0.2:
            self.__fps_count += 1

        if elapsed_time > 1.0:
            timer.reset_elapsed_time()

            return True

    def render_end(self):
        print(f"fps : {self.__fps_count}")
        self.__fps_count = 0.0


class game():
    def __init__(self):
        self.__render = renderer()
        self.__field = field()


    def run(self):
        is_continue = True
        timer.init()
        while is_continue:
            if not self.__render.render_begin():
                pass
            else:
                self.__field.print_field()
                # TypeError: __str__ returned non-string (type list)
                self.__render.render_end()
                clear()
                timer.reset_elapsed_time()


def main():
    G = game()
    G.run()


main()

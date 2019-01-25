from time import time
class Timer():
    def __init__(self):
        self.__prev_time = time()

    @staticmethod
    def capture_time(self):
        prev_time = __class__.prev_time
        current_time = time()
        __class__.elapsed_time = current_time - prev_time
        __class__.prev_time = current_time
    @staticmethod
    def get_elapsed_time(self):
        return __class__.elapsed_time

    prev_time = 0.0
    elapsed_time = 0.0
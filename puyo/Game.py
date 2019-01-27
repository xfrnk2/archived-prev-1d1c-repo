from timer import Timer
from field import PrintField

class Game():

    def __init__(self):
        self.__time = Timer.init()
        self.__field = PrintField

    def run(self):
        self.__field.test()


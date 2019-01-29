from mytimer import Timer
from field import PrintField
from renderer import renderer
class Game():

    aaa = PrintField()

    def __init__(self):
        self.__time = Timer.init()
        aaa = PrintField()

    def run(self):
        __class__.aaa.test()

    def render(self):
        if renderer.render_begin():
            __class__.run(self)

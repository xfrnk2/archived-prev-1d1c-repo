from mytimer import Timer
from field import PrintField
from renderer import renderer
class Game():

    field = None
    time = None

    def __init__(self):
        __class__.time = Timer.init()
        __class__.field = PrintField()
        renderer()

    def run(self):
        __class__.field.test()
        renderer.render_end()

    def render(self):
        while True:
            if renderer.render_begin():
                __class__.run()




import os
import threading
import keyboard
from copy import deepcopy
field_width, field_height = 6, 12
field = [['□' for _ in range(field_width)] for _ in range(field_height)]
cursorX, cursorY = 2, -2
checked = deepcopy(field)

class AsyncTask:

    def __init__(self):
        pass
    def TaskA(self):
        #로직 바꾸기
        global cursorY
        cursorY += 1
        threading.Timer(1,self.TaskA).start()

    def TaskB(self):
        print('Precess B')
        threading.Timer(3, self.TaskB).start()


def func():
    global checked, cursorX, cursorY

    at = AsyncTask()
    at.TaskA()
    at.TaskB()

    while True:
        os.system('cls')
        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("■", end='')
                else:
                    print(field[y][x], end='')
            print('')
        if keyboard.is_pressed('d'):
            cursorX += 1
        elif keyboard.is_pressed('a'):
            cursorX -= 1
        elif keyboard.is_pressed('w'):
            cursorY -= 1
        elif keyboard.is_pressed('s'):
            cursorY += 1

if __name__ == '__main__':
    func()

import os
import threading
import keyboard
from copy import deepcopy



class Block:
    def __init__(self):
        self.__block = "□"
    def __str__(self):
        return self.__block

field_width, field_height = 6, 12
field = [[Block() for _ in range(field_width)] for _ in range(field_height)]
cursorX, cursorY = 2, 0
checked = deepcopy(field)
another_block = "■"

class AsyncTask:

    def __init__(self):
        pass
    def TaskA(self):
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

    while True:
        os.system('cls')
        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("■", end='')
                else:
                    print(field[y][x], end='')
            print('')

        if set(field[x][2] for x in range(field_height)) == set(another_block):
            print("game over")

        if cursorY == 11 or field[cursorY+1][cursorX] == another_block:
            field[cursorY][cursorX] = another_block
            cursorX, cursorY = 2, -2


        if keyboard.is_pressed('d'):
            if cursorX != field_width-1 and field[cursorY][cursorX+1] != another_block:
                cursorX += 1
        elif keyboard.is_pressed('a'):
            if cursorX != 0 and field[cursorY][cursorX-1] != another_block:
                cursorX -= 1
        elif keyboard.is_pressed('s'):
            cursorY += 1

if __name__ == '__main__':
    func()

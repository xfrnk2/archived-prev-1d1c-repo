import os
import threading
import keyboard
from copy import deepcopy

from time import sleep

class Block:
    def __init__(self):
        self.__block = "□"
    def __str__(self):
        return self.__block

field_width, field_height = 6, 12
field = [[Block() for _ in range(field_width)] for _ in range(field_height)]
cursorX, cursorY = 2, 0
subCursorX, subCursorY = cursorX, cursorY-1
checked = deepcopy(field)
another_block = "■"

class AsyncTask:

    def __init__(self):
        pass
    def TaskA(self):
        global cursorY, subCursorY
        cursorY += 1
        subCursorY += 1
        threading.Timer(1,self.TaskA).start()

    def TaskB(self):
        print('Precess B')
        threading.Timer(3, self.TaskB).start()


def func():
    global checked, cursorX, cursorY, subCursorX, subCursorY

    at = AsyncTask()
    at.TaskA()

    while True:
        os.system('cls')
        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("■", end='')
                elif x == subCursorX and y == subCursorY:
                    print("■", end='')
                else:
                    print(field[y][x], end='')
            print('')

        if set(field[x][2] for x in range(field_height)) == set(another_block):
            print("game over")

        if cursorY == 11 or subCursorY == 11 or field[subCursorY+1][subCursorX] == another_block or field[cursorY+1][cursorX] == another_block:

            if cursorY == 11 or subCursorY == 11:
                field[cursorY][cursorX] = another_block
                field[subCursorY][subCursorX] = another_block

            elif abs(subCursorY-cursorY) == 1:
                field[cursorY][cursorX] = another_block
                field[subCursorY][subCursorX] = another_block

            elif field[cursorY+1][cursorX] == another_block and field[subCursorY+1][subCursorX] == another_block:
                field[cursorY][cursorX] = another_block
                field[subCursorY][subCursorX] = another_block

            elif field[cursorY+1][cursorX] == another_block:
                field[cursorY][cursorX] = another_block

                for v in range(field_height-1, subCursorY, -1):

                    if field[v][subCursorX] != another_block:
                        field[v][subCursorX] = another_block
                        break
            elif field[cursorY+1][cursorX] != another_block:
                field[subCursorY][subCursorX] = another_block

                for v in range(field_height - 1, subCursorY, -1):
                    if field[v][cursorX] != another_block:
                        field[v][cursorX] = another_block
                        break


            cursorX, cursorY = 2, -1
            subCursorX, subCursorY = cursorX, cursorY+1
        # if cursorY == 11 or subCursorY == 11 or field[cursorY+1][cursorX] == another_block or field[subCursorY+1][cursorX] == another_block:
        #
        #     if abs(cursorX-subCursorX) == 1:
        #
        #         if cursorY == subCursorY == 11:
        #             field[cursorY][cursorX] = another_block
        #             field[subCursorY][subCursorX] = another_block
        #
        #
        #         elif field[cursorY+1][cursorX] == another_block and field[subCursorY+1][subCursorX] != another_block:
        #             field[cursorY][cursorX] = another_block
        #
        #
        #             for y in range(subCursorY+1, field_height):
        #                 if y == field_height - 1:
        #                     field[y][subCursorX] = another_block
        #
        #
        #                 elif field[y+1][subCursorX] == another_block:
        #                     field[y][subCursorX] = another_block
        #
        #
        #
        #         elif field[subCursorY+1][subCursorX] == another_block and field[cursorY+1][cursorX] != another_block:
        #             field[subCursorY][subCursorX] = another_block
        #
        #             for y in range(cursorY+1, field_height):
        #
        #                 if y == field_height - 1:
        #                     field[y][cursorX] = another_block
        #
        #
        #                 elif field[y+1][cursorX] == another_block:
        #                     field[y][cursorX] = another_block
        #
        #
        #     else:
        #         if cursorY == 11 or subCursorY == 11 or field[cursorY+1][cursorX] == another_block or field[subCursorY+1][cursorX] == another_block:
        #             field[cursorY][cursorX] = another_block
        #             field[subCursorY][subCursorX] = another_block
        #
        #     cursorX, cursorY = 2, -1
        #     subCursorX, subCursorY = cursorX, cursorY+1


        if keyboard.is_pressed('RIGHT'):
            if abs(cursorY - subCursorY) == 1:

                if cursorX != field_width-1 and field[cursorY][cursorX+1] != another_block:
                    cursorX += 1
                    subCursorX += 1
            else:
                if cursorX > subCursorX:
                    if cursorX != field_width - 1 and field[cursorY][cursorX+1] != another_block:
                        cursorX += 1
                        subCursorX += 1
                elif cursorX < subCursorX:
                    if subCursorX != field_width - 1 and field[subCursorY][subCursorX + 1] != another_block:
                        cursorX += 1
                        subCursorX += 1


        elif keyboard.is_pressed('LEFT'):



            if abs(cursorY - subCursorY) == 1:

                if cursorX != 0 and field[cursorY][cursorX-1] != another_block:
                    cursorX -= 1
                    subCursorX -= 1
            else:
                if cursorX > subCursorX:
                    if subCursorX != 0 and field[subCursorY][subCursorX - 1] != another_block:
                        cursorX -= 1
                        subCursorX -= 1
                elif cursorX < subCursorX:
                    if cursorX != 0 and field[cursorY][cursorX - 1] != another_block:
                        cursorX -= 1
                        subCursorX -= 1




        elif keyboard.is_pressed('DOWN'):
            cursorY += 1
            subCursorY += 1

        if keyboard.is_pressed('z'):
            if cursorY > subCursorY:
                if 0 < cursorX and field[cursorY][cursorX - 1] != another_block:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY + 1
            elif cursorY < subCursorY:
                if cursorX < field_width-1  and field[cursorY][cursorX + 1] != another_block:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY - 1
            elif cursorY == subCursorY:

                if subCursorX < cursorX:
                    if cursorY != field_height-1 and field[cursorY-1][cursorX] != another_block:
                        subCursorX, subCursorY = subCursorX +1, subCursorY +1

                elif subCursorX > cursorX:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY - 1

if __name__ == '__main__':
    func()

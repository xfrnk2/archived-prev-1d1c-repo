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



        if cursorY == 11 or subCursorY == 11 or field[cursorY+1][cursorX] == another_block :


            field[cursorY][cursorX] = another_block
            field[subCursorY][subCursorX] = another_block


            cursorX, cursorY = 2, -2
            subCursorX, subCursorY = cursorX, cursorY-1
        #
        # #가로
        # elif field[cursorY + 1][cursorX] == another_block or field[subCursorY + 1][subCursorX] == another_block:
        #
        #     if abs(cursorX - subCursorX) == 1:
        #
        #         if field[subCursorY + 1][subCursorX] == another_block:
        #             field[subCursorY][subCursorX] = another_block
        #             for y in range(cursorY, field_height):
        #                 if field[y][cursorX] == another_block:
        #                     field[y-1][cursorX] = another_block
        #         else:
        #             field[cursorY][cursorX] = another_block
        #             for y in range(subCursorY, field_height):
        #                 if field[y][subCursorX] == another_block:
        #                     field[y - 1][subCursorX] = another_block
        #     else:
        #         field[cursorY][cursorX] = another_block
        #         field[subCursorY][subCursorX] = another_block
        #     cursorX, cursorY = 2, -2
        #     subCursorX, subCursorY = cursorX, cursorY-1
        #

        if keyboard.is_pressed('RIGHT'):
            if subCursorY + 1 == cursorY:

                if cursorX != field_width-1 and field[cursorY][cursorX+1] != another_block:
                    cursorX += 1
                    subCursorX += 1
            else:
                if cursorX - 1 == subCursorX:
                    if 0 < cursorX < field_width - 1 and field[cursorY][cursorX + 1] != another_block:
                        cursorX += 1
                        subCursorX += 1
                else:
                    if 0 < subCursorX <= field_width - 1 and field[subCursorY][subCursorX + 1] != another_block:
                        cursorX += 1
                        subCursorX += 1


        elif keyboard.is_pressed('LEFT'):



            if subCursorY + 1 == cursorY:

                if cursorX != 0 and field[cursorY][cursorX-1] != another_block:
                    cursorX -= 1
                    subCursorX -= 1
            else:
                if cursorX - 1 == subCursorX:
                    if 0 < subCursorX < field_width-1 and field[subCursorY][subCursorX - 1] != another_block:
                        cursorX -= 1
                        subCursorX -= 1
                else:
                    if 0 <= cursorX < field_width-1 and field[cursorY][cursorX - 1] != another_block:
                        cursorX -= 1
                        subCursorX -= 1




        elif keyboard.is_pressed('DOWN'):
            cursorY += 1
            subCursorY += 1

        if keyboard.is_pressed('z'):
            if cursorY-1 == subCursorY:
                if 0 < cursorX and field[cursorY][cursorX - 1] != another_block and field[cursorY-1][cursorX-1] != another_block:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY + 1
            elif cursorY+1 == subCursorY:
                if 0 < cursorX and field[cursorY][cursorX - 1] != another_block and field[cursorY-1][cursorX-1] != another_block:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY - 1
            elif cursorY == subCursorY and abs(cursorX-subCursorX)==1:
                if subCursorX + 1 == cursorX:
                    if cursorY != 0:
                        subCursorX, subCursorY = subCursorX +1, subCursorY +1
                        # subCursorX, cursorX = cursorX, subCursorX
                        # subCursorY, cursorY = cursorY, subCursorY

                elif subCursorX - 1 == cursorX:
                    if field[subCursorY - 1][subCursorX] != another_block:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY - 1

if __name__ == '__main__':
    func()

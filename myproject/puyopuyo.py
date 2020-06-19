import os
import threading
import keyboard
from copy import deepcopy
from random import randrange
import sys
from time import sleep
class Block:
    def __init__(self):
        self.__block = "□"

    def set_block(self, shape):
        self.__block = shape

    def get_shape(self):
        return self.__block

    def clear_block(self):
        self.__block = "□"

    def __str__(self):
        return self.__block

lock = threading.Lock()
field_width, field_height = 6, 12
empty_field = [[Block() for _ in range(field_width)] for _ in range(field_height)]
field = deepcopy(empty_field)
cursorX, cursorY = 2, 0
subCursorX, subCursorY = cursorX, cursorY-1
another_block = "■"
shape_list = []
blocked_list = []

class AsyncTask:

    def __init__(self):
        self.__timer = None
    def TaskA(self):
        global cursorY, subCursorY
        cursorY += 1
        subCursorY += 1
        self.__timer = threading.Timer(1,self.TaskA)
        self.__timer.start()
        # threading.Timer(1,self.TaskA).start()
    def stopTaskA(self):
        self.__timer.cancel()


def checkField(x: int, y: int, shape:str):

    if x < 0 or y < 0 or field_width-1< x or field_height-1 < y or field[y][x].get_shape() != shape or (x, y) in blocked_list or (x, y) in shape_list:
        return False
    else:
        shape_list.append((x, y))
        if checkField(x-1, y, shape) or checkField(x, y+1, shape) or checkField(x+1, y, shape)or checkField(x, y-1, shape):
            return True
        blocked_list.append((x, y))
        return False

def ignition():
    if 4 <= len(shape_list):
        for value in shape_list:
            x, y = value
            field[y][x].clear_block()
            for i in range(y, 0, -1):
                field[i][x], field[i - 1][x] = field[i - 1][x], field[i][x]
    return

def func():
    global cursorX, cursorY, subCursorX, subCursorY, field, shape_list, blocked_list

    at = AsyncTask()
    at.TaskA()

    blocks = ["♥", "◆", "●", "♣"]
    current_block = (blocks[randrange(4)], blocks[randrange(4)])
    while True:
        os.system('cls')

        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print(current_block[0], end='')
                elif x == subCursorX and y == subCursorY:
                    print(current_block[1], end='')
                else:
                    print(field[y][x], end='')
            print('')








        if cursorY == 11 or subCursorY == 11 or field[subCursorY+1][subCursorX].get_shape() in blocks or field[cursorY+1][cursorX].get_shape() in blocks:

            if cursorY == 11 or subCursorY == 11:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif abs(subCursorY-cursorY) == 1:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif field[cursorY+1][cursorX].get_shape() in blocks and field[subCursorY+1][subCursorX].get_shape() in blocks:
                field[cursorY][cursorX].set_block(current_block[0])
                field[subCursorY][subCursorX].set_block(current_block[1])

            elif field[cursorY+1][cursorX].get_shape() in blocks and field[subCursorY+1][subCursorX].get_shape() not in blocks:
                field[cursorY][cursorX].set_block(current_block[0])

                for v in range(field_height-1, subCursorY, -1):

                    if field[v][subCursorX].get_shape() not in blocks:
                        field[v][subCursorX].set_block(current_block[1])
                        break
            elif field[subCursorY+1][subCursorX].get_shape() in blocks and field[cursorY+1][cursorX].get_shape() not in blocks:
                field[subCursorY][subCursorX].set_block(current_block[1])

                for v in range(field_height - 1, subCursorY, -1):
                    if field[v][cursorX].get_shape() not in blocks:
                        field[v][cursorX].set_block(current_block[0])
                        break



            for pair in [("cursorX", "cursorY"), ("subCursorX", "subCursorY")]:
                x, y = pair
                eval(f"checkField({x}, {y}, field[{y}][{x}].get_shape())")
                ignition()
                shape_list = []
                blocked_list = []

            # for y in range(field_height):
            #     for x in range(field_width):
            #         if field[y][x].get_shape() in blocks:
            #             checkField(x, y, field[y][x].get_shape())
            #
            #             if 4 <= len(shape_list):
            #                 # shape_list.sort(key = lambda value : (-value[1],value[0]))
            #                 location = 0
            #                 l, r = 11, 0
            #                 for value in shape_list:
            #                     x, y = value
            #                     field[y][x].clear_block()
            #                 for j in range(y):
            #                     if field[j][x].get_shape() in blocks:
            #                         location = j
            #                         break
            #                 for i in range(y, -1, -1):
            #                     if field[i][x].get_shape() not in blocks:
            #                         l = i
            #                     if field[i][x].get_shape() in blocks:
            #                         r = i + 1
            #
            #                 #모든 상쇄된 블록들은 일괄적으로 처리할수 있는 방법으로 구현하기
            #                     # for i in range(y, 0, -1):
            #                     #     field[i][x], field[i - 1][x] = field[i - 1][x], field[i][x]


                        #
                        # shape_list = []
                        # blocked_list = []



            cursorX, cursorY = 2, -1
            subCursorX, subCursorY = cursorX, cursorY+1
            current_block = (blocks[randrange(4)], blocks[randrange(4)])














        # if set(field[x][2] for x in range(field_height)) == set(another_block):
        if "□" not in [field[x][2].get_shape() for x in range(field_height)]:

                while True:
                    flag = input("game over. Retry? (Y/N)")
                    if flag == "N":
                        at.stopTaskA()
                        sys.exit()
                    elif flag == "Y":
                        field = deepcopy(empty_field)
                        cursorX, cursorY = 2, -1
                        subCursorX, subCursorY = cursorX, cursorY + 1
                        break
                    else:
                        print("You should input Y or N")




        if keyboard.is_pressed('RIGHT'):
            if abs(cursorY - subCursorY) == 1:

                if cursorX != field_width-1 and field[cursorY][cursorX+1].get_shape() not in blocks:
                    cursorX += 1
                    subCursorX += 1
            else:
                if cursorX > subCursorX:
                    if cursorX != field_width - 1 and field[cursorY][cursorX+1].get_shape() not in blocks:
                        cursorX += 1
                        subCursorX += 1
                elif cursorX < subCursorX:
                    if subCursorX != field_width - 1 and field[subCursorY][subCursorX + 1].get_shape() not in blocks:
                        cursorX += 1
                        subCursorX += 1


        elif keyboard.is_pressed('LEFT'):



            if abs(cursorY - subCursorY) == 1:

                if cursorX != 0 and field[cursorY][cursorX-1].get_shape() not in blocks:
                    cursorX -= 1
                    subCursorX -= 1
            else:
                if cursorX > subCursorX:
                    if subCursorX != 0 and field[subCursorY][subCursorX - 1].get_shape() not in blocks:
                        cursorX -= 1
                        subCursorX -= 1
                elif cursorX < subCursorX:
                    if cursorX != 0 and field[cursorY][cursorX - 1].get_shape() not in blocks:
                        cursorX -= 1
                        subCursorX -= 1




        elif keyboard.is_pressed('DOWN'):
            cursorY += 1
            subCursorY += 1

        if keyboard.is_pressed('z'):
            if cursorY > subCursorY:
                if 0 < cursorX and field[cursorY][cursorX - 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY + 1
            elif cursorY < subCursorY:
                if cursorX < field_width-1  and field[cursorY][cursorX + 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY - 1
            elif cursorY == subCursorY:

                if subCursorX < cursorX:
                    if cursorY != field_height-1 and field[cursorY+1][cursorX].get_shape() not in blocks:
                        subCursorX, subCursorY = subCursorX +1, subCursorY +1

                elif subCursorX > cursorX:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY - 1

        if keyboard.is_pressed('x'):
            if cursorY > subCursorY:
                if cursorX < field_width-1 and field[cursorY][cursorX + 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX + 1, subCursorY + 1
            elif cursorY < subCursorY:
                if 0 <cursorX and field[cursorY][cursorX - 1].get_shape() not in blocks:
                    subCursorX, subCursorY = subCursorX - 1, subCursorY - 1
            elif cursorY == subCursorY:

                if subCursorX < cursorX:
                    subCursorX, subCursorY = subCursorX +1, subCursorY -1

                elif subCursorX > cursorX:
                    if cursorY != field_height - 1 and field[cursorY + 1][cursorX].get_shape() not in blocks:
                        subCursorX, subCursorY = subCursorX - 1, subCursorY + 1

if __name__ == '__main__':
    func()

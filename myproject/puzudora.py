import keyboard
import os
from enum import Enum
from random import randrange
from copy import deepcopy
field_width, field_height = 8, 8
blocks = {0: '·', 1: '●', 2: '◆', 3: '▲'}
field = [[blocks[randrange(1,4)] for _ in range(field_width)] for _ in range(field_height)]
checked = deepcopy(field)
def getConnectedBlockCount(x:int, y:int, blockType:str, count:int) -> int:
    if x < 0 or field_width <= x or y < 0 or field_height <= y or checked[y][x] == 1 or field[y][x] == blocks[0] or field[y][x] != blockType:
        return count
    count += 1
    checked[y][x] = 1

    count = getConnectedBlockCount(x, y - 1, blockType, count)
    count = getConnectedBlockCount(x - 1, y, blockType, count)
    count = getConnectedBlockCount(x, y + 1, blockType, count)
    count = getConnectedBlockCount(x + 1, y, blockType, count)

    return count

def run():
    global checked
    cursorX, cursorY = 0, 0
    selectedX, selectedY = -1, -1


    while True:
        os.system('cls')

        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("◎", end='')
                else:
                    print(field[y][x], end='')
            if y == selectedY:
                print("←", end='')
            print("")
        for x in range(field_width):
            if x == selectedX:
                print("↑", end='')
            else:
                print("　", end='')
        print("")


        if keyboard.is_pressed('d'):
            cursorX += 1
        elif keyboard.is_pressed('a'):
            cursorX -= 1
        elif keyboard.is_pressed('w'):
            cursorY -= 1
        elif keyboard.is_pressed('s'):
            cursorY += 1


        if keyboard.is_pressed('enter'):
            if selectedX < 0:
                selectedX, selectedY = cursorX, cursorY
            else:
                field[cursorY][cursorX], field[selectedY][selectedX]= field[selectedY][selectedX], field[cursorY][cursorX]

                checked = [[0 for _ in range(field_width)]for _ in range(field_height)]
                for y in range(field_height):
                    for x in range(field_width):
                        n = getConnectedBlockCount(x, y, field[y][x], 0)
                        if 3 <= n:
                            field[y][x] = blocks[0]
                selectedX = selectedY = -1
def main():
    run()
main()
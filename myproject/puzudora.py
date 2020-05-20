import keyboard
import os
from enum import Enum
from random import randrange

def run():
    blocks = {0 : '·', 1 : '●', 2 : '◆', 3 : '▲'}
    cursorX, cursorY = 0, 0
    field_width, field_height = 8, 8
    field = [[blocks[randrange(1,4)] for _ in range(field_width)] for _ in range(field_height)]

    while True:
        os.system('cls')

        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("◎", end='')
                else:
                    print(field[y][x], end='')
            print("")

        if keyboard.is_pressed('d'):
            cursorX += 1
        elif keyboard.is_pressed('a'):
            cursorX -= 1
        elif keyboard.is_pressed('w'):
            cursorY -= 1
        elif keyboard.is_pressed('s'):
            cursorY += 1

def main():
    run()
main()
import keyboard
import os
from enum import Enum
from random import randrange

class Block(Enum):
    block_none = "·"
    blockA = "●"
    blockB = "◆"
    blockC = "▲"

def run():
    # randrange(len(Block.__members__))


    cursorX, cursorY = 0, 0
    c = 0
    while True:

        os.system('cls')

        field_width = 8
        field_height = 8

        for y in range(field_height):
            for x in range(field_width):
                if x == cursorX and y == cursorY:
                    print("◎", end='')
                else:
                    print("·", end='')
            print("")
        c += 1
        print(c)

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

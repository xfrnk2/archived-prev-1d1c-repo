from time import time
import os

class Block:
    def __init__(self):
        self.__data = '□'

    def __str__(self):
        return self.__data

    def set_data(self, input_data):
        self.__data = input_data


class Field:
    def __init__(self, size):
        self.__size = size
        self.__data = [[Block() for _ in range(size)] for _ in range(size)]
        self.__elapsed_time = 0
        self.__start_time = 0
    def print(self):
        for array in self.__data:
            for block in array:
                print(block, end='')
            print('')
        print('--------------------')

    def set_start_time(self):
        self.__start_time = time()

    def set_elapsed_time(self):
        current_time = time()
        self.__elapsed_time = current_time - self.__start_time

    def get_elapsed_time(self):
        return self.__elapsed_time

    def change_data(self, y):
        self.__data[y][2].set_data('■')

    def reset(self):
        self.__data = [[Block() for _ in range(self.__size)] for _ in
                       range(self.__size)]


def clear():
    os.system('cls')

if __name__ == '__main__':

    f = Field(5)

    for x in range(5):
        # f.set_start_time()

        # f.set_elapsed_time()
        # if f.get_elapsed_time() > 0:
            f.reset()
            f.change_data(x)
            f.print()

            if x == 4:
                break

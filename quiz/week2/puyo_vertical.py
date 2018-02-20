
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

    def print(self):
        for array in self.__data:
            for block in array:
                print(block, end='')
            print('')
        print('--------------------')

    def change_data(self):
        for x, array in enumerate(self.__data):

            for y, block in enumerate(array):

                    if y == 2:
                        block.set_data('■')





    def reset(self):
        self.__data = [[Block() for _ in range(self.__size)] for _ in
                       range(self.__size)]


if __name__ == '__main__':

    f = Field(5)

    f.reset()
    f.change_data()
    f.print()

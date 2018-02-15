"""
화면에 아래와 같이 출력합니다.

*
**
***
****
*****

*****
****
***
**
*


    *
   **
  ***
 ****
*****

*****
 ****
  ***
   **
    *


단 아래와 같은 방법으로 출력하지 않습니다.

print( '*' );
print( '**' );
print( '***' );
print( '****' );
print( '*****' );


for, list() 등의 기능을 적극 활용합니다.

"""


class Block:
    def __init__(self):
        self.__data = ' '

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

    def change_data(self, solve_func):
        for y, array in enumerate(self.__data):
            for x, block in enumerate(array):
                if solve_func(x, self.__size - 1 - y):
                    block.set_data('*')

    def reset(self):
        self.__data = [[Block() for _ in range(self.__size)] for _ in
                       range(self.__size)]


if __name__ == '__main__':

    #
    # f.change_data( lambda x, y: y >= 0.3 * x + 10 )
    # f.print() 

    f = Field(5)

    # solve 1
    f.reset()
    f.change_data(lambda x, y: y <= -x + 5)
    f.print()

    # solve 2
    # 중략

    # solve 3
    # 중략

"""
숫자를 입력 받아 화면에 아래와 같이 출력합니다.
숫자의 출력 범위는 x를 입력 받아 x^2(x의 제곱수) 만큼 출력합니다.

즉 5를 입력 받아 1~25까지 출력합니다.

1. 숫자를 입력 받는다
2. 숫자를 제곱한다
3. 일정 범위의 숫자를 화면의 특정 위치별로 출력한다
4. 좌표를 계산한다
  4.1 좌표가 좌우로 움직인다
  4.2 좌표가 상하로 움직인다.


25 24 23 22 21
10  9  8  7 20
11  2  1  6 19
12  3  4  5 18
13 14 15 16 17

이와 같이 숫자가 회오리 치듯이 출력 되어야 합니다.





4를 입력 받으면 아래와 같이 출력합니다.

16 15 14 13
 5  4  3 12
 6  1  2 11
 7  8  9 10



반대 방향으로도 출력해 봅니다.

25 10 11 12 13
24  9  2  3 14
23  8  1  4 15
22  7  6  5 16
21 20 19 18 17


16  5  6  7
15  4  1  8
14  3  2  9
13 12 11 10

몫을 구할때 //, 나머지를 구할때 %

for, list() 등의 기능을 적극 활용합니다.



x = 4
array = [ [ 0 ] * x for _ in range( x ) ]


# array = range(1,x*x)
# for _ in range(1, x+1):

# position =
def set_value_in_position( x, y, value ):
    # array[ y * 3 + x ] = value
    array[ x ][ y ] = value


# set_value_in_position(1,1,10)


# 수평 방향으로 -1
set_value_in_position(1,0,v[1])
# 수직 방향으로 +1
set_value_in_position(2,0,v[2])
# 수평 방향으로 +2
set_value_in_position(2,1,v[3])
set_value_in_position(2,2,v[4])
# 수직 방향으로 -2
set_value_in_position(1,2,v[5])
set_value_in_position(0,2,v[6])
# 수평 방향으로 -3
set_value_in_position(0,1,v[7])
set_value_in_position(0,0,v[8])

a[1][1]=1
# 수평 방향으로 -1
a[1][0]=2
# 수직 방향으로 +1
a[2][0]=3
# 수평 방향으로 +2
a[2][1]=4
a[2][2]=5
# 수직 방향으로 -2
a[1][2]=6
a[0][2]=7
# 수평 방향으로 -3
a[0][1]=8
a[0][0]=9


for j in range( 0, x ):
    print( array[ j ] )


size = 5
array = ['' for _ in range(25,0,-1)]


def printfield() -> None:
    for array in [["*" for _ in range(size)] for _ in range(size)]:
        for block in array:
            print(block, end='')
        print('')

    print()


print(array[1])


# set_value_in_position(1,1,10)


def printfield(size):
    for array in [["*" for _ in range(size)] for _ in range(size)]:
        for block in array:
            print(block, end='')
        print('')

    print()




print(printfield(size))



print(numbers())


# position =

while True:
    size = int(input("출력할 크기는? :"))
    if size == 0 :
        print("good bye~")
        break
    if size<3 or size>9:
        print("3에서 9 사이만 인정")
        continue

    a = [[0]*size for _ in range(size)]
    start = (size-1)//2
    c = -1
    h = start
    v = start
    n = 0
    n = n + 1
    a[v][h]=n
    for i in range(1, size + 1 ):
        c = c * (-1)

        for _ in range(0,i):
            h = h+1*c
            if size**2==n:

                break
            n = n+1
            a[v][h]= n
        for _ in range(0,i):
            v=v+1*c
            if size**2==n:
                break
            n=n+1
            a[v][h]=n
    print("")
    for j in range(0, size):

        print(a[j])


"""

# 1~25까지의 숫자를 그룹을 만들거나 정해진 규칙으로 나타나게 한다.


# while True:
#     size = int(input("출력할 크기는? :"))
#     if size == 0 :
#         print("good bye~")
#         break
#     if size<3 or size>9:
#         print("3에서 9 사이만 인정")
#         continue
#
#     a = [[0]*size for _ in range(size)]
#     start = (size-1)//2
#     c = -1
#     h = start
#     v = start
#     n = 0
#     n = n + 1
#     a[v][h]=n
#     for i in range(1, size + 1 ):
#         c = c * (-1)
#
#         for _ in range(0,i):
#             h = h+1*c
#             if size**2==n:
#
#                 break
#             n = n+1
#             a[v][h]= n
#         for _ in range(0,i):
#             v=v+1*c
#             if size**2==n:
#                 break
#             n=n+1
#             a[v][h]=n
#     print("")
#     for j in range(0, size):
#
#         print(a[j])


# 문제를 푼다.
# 1. 숫자를 입력 받는다
# 2. 숫자를 제곱한다
# 3. 일정 범위의 숫자를 화면의 특정 위치별로 출력한다
# 4. 좌표를 계산한다
#   4.1 좌표가 좌우로 움직인다
#   4.2 좌표가 상하로 움직인다.

import math

# TODO - 아래쪽 코드가 우아하지 않으니 고쳐주세요!
X_TURN = 0
Y_TURN = 1


class Coordinator():
    def __init__(self, size):
        self.__size = size
        self.__x_move_counts = [x for x in range(size, 0, -1)]
        self.__y_move_counts = [x for x in range(size - 1, 0, -1)]
        self.__x_move_count = self.__x_move_counts.pop(0)
        self.__y_move_count = self.__y_move_counts.pop(0)
        self.__current_turn = X_TURN
        self.__x_position = 0
        self.__y_position = 0
        self.__x_possitive = True
        self.__y_possitive = True

    def calc_coord(self):
        if self.__current_turn == X_TURN:
            self.move_x()
        else:
            self.move_y()

    def move_x(self):

        self.__x_move_count -= 1

        if self.__x_move_count == 0:
            self.__x_possitive = not self.__x_possitive
            self.__current_turn = Y_TURN
            self.__x_move_count = self.__x_move_counts.pop(0)
        else:
            if self.__x_possitive:
                self.__x_position += 1
            else:
                self.__x_position -= 1

    def move_y(self):
        self.__y_move_count -= 1

        if self.__y_move_count == 0:
            self.__y_possitive = not self.__y_possitive
            self.__current_turn = X_TURN
            self.__y_move_count = self.__y_move_counts.pop(0)
        else:
            if self.__y_possitive:
                self.__y_position += 1
            else:
                self.__y_position -= 1

    def get_coord(self):
        return self.__x_position, self.__y_position


class Resolver():
    def __init__(self):
        self.__data = None
        self.__data = None
        self.__data = None

    @staticmethod
    def pow(data):
        assert isinstance(data, int), f"숫자가 들어와야 하는데 {data}를 입력했습니다."
        return int(math.pow(int(data), 2))

    def input_number(self):
        try:
            self.__data = int(input())
            return __class__.pow(self.__data)

        except ValueError:
            print(f"{self.__data}가 숫자가 아니라서 일단 0으로 처리합니다.")
            return 0

    @staticmethod
    def print_value(value):
        print(value)

    @staticmethod
    def draw_value(value):
        pass

    def solve(self):
        input_result = self.input_number()
        __class__.print_value(input_result)

        self.draw_field()

    def draw_field(self):
        assert self.__data > 0, f'{self.__data}는 0보다 커야 합니다'
        field = ["*" for _ in range(self.__data) for _ in range(self.__data)]
        print(field)


if __name__ == '__main__':

    coordinator = Coordinator(4)

    for _ in range(16):
        print(coordinator.get_coord())
        coordinator.calc_coord()

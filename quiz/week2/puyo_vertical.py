# 필드를 네모로 출력한다
# 출력한 네모를 까만 네모로 바꿔 끼운다

# 리스트를 만든다. 5x5의 리스트. 다음은 위치를 지정한다. 배열 만들기 -> 배열 순서 -> 클리어

import time
import os

def clear():
    os.system('cls')

wall = "□"
field = [[wall for _ in range(5)] for _ in range(5)]
block = "■"


# 0, 2
# 1, 2
#  2, 2
#   3, 2
#    4, 2


def print_field():
    a = 0
    b = 2

    count_value = 6

    for x in range(5):
        for y in range(0, 14, 3):
            if x == y:
                clear()
                for data in field:
                    output = ''.join(data) + '\n'
                    print(output)

                time.sleep(1)
                count_value -= 1

            if y:
                field[a][b] = block

                try:
                    field[a - 2][b] = wall
                except IndexError:
                    pass

                clear()
                for data in field:
                    output = ''.join(data) + '\n'
                    print(output)

                time.sleep(1)
                count_value -= 1
                a += 1

            if count_value == 0:
                break


if __name__ == '__main__':
    print_field()

    # join의 사용법
    l = [ 'hello', 'world', '1234']

    result1 = ' '.join(l)
    result2 = ','.join(['a', 'b', 'c'])

    print(result1)
    print(result2)

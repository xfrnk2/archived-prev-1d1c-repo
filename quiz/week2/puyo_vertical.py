# 필드를 네모로 출력한다
# 출력한 네모를 까만 네모로 바꿔 끼운다

# 리스트를 만든다. 5x5의 리스트. 다음은 위치를 지정한다. 배열 만들기 -> 배열 순서 -> 클리어

# https://docs.python.org/3/howto/curses.html
import curses
from curses import wrapper
import time

stdscr = curses.initscr()

field = [["□" for _ in range(5)] for _ in range(5)]
block = "■"


# 0, 2
# 1, 2
#  2, 2
#   3, 2
#    4, 2


def print_field(stdscr):
    a = 0
    b = 2

    count_value = 6
    stdscr.refresh()
    stdscr.clear()

    for x in range(5):
        for y in range(0, 14, 3):
            if x == y:
                for data in field:
                    output = ''.join(data) + '\n'

                    stdscr.addstr(output)
                    stdscr.refresh()

                time.sleep(1)
                count_value -= 1

            if y:
                field[a][b] = block

                for data in field:
                    output = ''.join(data) + '\n'

                    stdscr.addstr(output)
                    stdscr.refresh()

                time.sleep(1)
                count_value -= 1
                a += 1

            if count_value == 0:
                break

            stdscr.clear()


if __name__ == '__main__':
    wrapper(print_field)
    # print_field()

    # join의 사용법
    result1 = ' '.join(['hello', 'world'])
    result2 = ','.join(['a', 'b', 'c'])

    print(result1)
    print(result2)

# AT TEST WITH JS: TODO - 1. 숫자 사각형 그리기(빙글빙글 돌아서 가장 안으로 나가는 , n을 입력 받기)
import copy
class Direction:
    def __init__(self):
        self.direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.idx = 0
        self.next = self.direction[self.idx]

    def turn(self):
        self.idx += 1
        if 4 <= self.idx:
            self.idx -= 4
        self.next = self.direction[self.idx]


def solution(n: int):

    field = [[0] * n for _ in range(n)]

    direction = Direction()
    cnt = 1
    coordinate = [0, 0]
    field[0][0] = 1


    while cnt < n * n:
        nx, ny = coordinate[0] + direction.next[0], coordinate[1] + direction.next[1]
        if nx < 0 or n <= nx or ny < 0 or n <= ny or 0 < field[ny][nx]:
            direction.turn()
            continue
        coordinate = [nx, ny]
        cnt += 1
        field[ny][nx] = cnt

    for i in field:
        print(i)

solution(4)

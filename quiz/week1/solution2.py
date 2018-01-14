# coding=utf-8


from enum import Enum
from math import pow


class Position:
    """
    좌표를 담아 전달하기 위한 객체
    namedTuple 을 쓰고 싶지만 tuple 자료구조는 값 수정이 안 되므로 클래스를 사용했다.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self) -> (int, int):
        return self.x, self.y

class Item:
    """
    숫자 데이터를 담당하는 객체
    """

    def __init__(self, data=None):
        self.__data = data

    def __str__(self):
        return f'{self.__data:2}'

    def __repr__(self):
        return f'{self.__data:2}'

    def set(self, data):
        assert_type(data, int, 'int')
        self.__data = data

    def get(self) -> int:
        return self.__data


class Direction(Enum):
    RIGHT = 1
    BOTTOM = 2
    TOP = 3
    LEFT = 4


def assert_type(value, type: object, name: str) -> None:
    assert isinstance(value, type), \
        f'{name}({value}) {type(value)} is not {type}'


def get_next_position(position: Position, direction: Direction) -> Position:
    assert_type(position, Position, 'Position')
    assert_type(direction, Direction, 'Direction')

    x, y = position.get()
    direction_to_position = {
        Direction.RIGHT: Position(x + 1, y),
        Direction.BOTTOM: Position(x, y + 1),
        Direction.LEFT: Position(x - 1, y),
        Direction.TOP: Position(x, y - 1)
    }

    return direction_to_position[direction]


def get_next_direction(direction: Direction) -> Direction:
    assert_type(direction, Direction, 'Direction')

    directions = list(Direction)
    index = directions.index(direction)
    index = (index + 1) % len(directions)

    return directions[index]


def get_next_position_value(matrix: list, position: Position,
                            direction: Direction) -> Item:
    """
    진행 방향에 놓인 다음 위치의 값을 반환

    :param matrix:전체 영역
    :param position:현재 위치
    :param direction:진행 방향
    :return:다음 위치의 값을 담은 객체
    """
    assert_type(matrix, list, 'matrix')
    assert_type(position, Position, 'Position')
    assert_type(direction, Direction, 'Direction')

    next_position = get_next_position(position, direction)
    x, y = next_position.get()

    # 영역 초과, 인덱스는 0 이하로 내려갈 수 없음
    if x < 0 or y < 0:
        raise IndexError

    # 2차원 리스트에 접근해서 값 가져옴. 범위 넘어가면 IndexError 발생
    value: Item = matrix[y][x]

    # 이미 값이 채워진 영역이면 진입 실패, IndexError 발생시킨다
    if value.get() is not None:
        raise IndexError

    return matrix[y][x]


def step_over(matrix: list, index: int, position: Position,
              direction: Direction) -> bool:
    """
    한 블록 이동하면서 숫자를 채운다.
    이동 가능했으면(정상적으로 숫자를 채웠으면) True 반환
    이동 불가능했으면(숫자 채우기 실패) False 반환

    :param matrix:전체 영역
    :param index:현재 찍을 숫자
    :param position:현재 위치
    :param direction:진행 방향
    :return:숫자 채우기 성공 실패 여부
    """
    assert_type(matrix, list, 'matrix')
    assert_type(index, int, 'index')
    assert_type(position, Position, 'Position')

    try:
        # NOTE - 다음 위치의 값을 꺼내본다. 유효한 영역이 아니면 IndexError 발생
        item = get_next_position_value(matrix, position, direction)

        # 해당 위치에 적절한 값을 넣고, 현재 위치를 해당 위치로 갱신
        item.set(index)
        next_position = get_next_position(position, direction)
        position.x, position.y = next_position.get()

        # 이동 가능했다
        return True

    # 유효한 영역이 아님
    except IndexError:
        # 이동 불가능했다.
        return False


def print_matrix(matrix: list) -> None:
    assert_type(matrix, list, 'matrix')

    for line in matrix:
        output = ''

        for item in line:
            output += f'{item} '

        print(output)
    print('')


def solve(size: int, direction: Direction, decrease: bool = True) -> None:
    assert_type(size, int, 'size')
    assert_type(direction, Direction, 'Direction')
    assert size > 0, f'{size} must positive'

    # 전체 영역 초기화
    matrix = [[Item() for _ in range(size)] for _ in range(size)]

    # n**2 크기만큼 숫자를 찍어야 함
    max_count = int(pow(size, 2))

    # 차례대로 찍을 숫자 범위를 미리 지정
    # 감소
    if decrease:
        max_range = range(max_count, 0, -1)
    # 증가
    else:
        max_range = range(1, max_count + 1)

    # 여기를 수정하면, 시작 위치를 지정 가능하다.
    position = Position(x=0, y=0)
    x, y = position.get()

    # 최초의 1개와 나머지 n**2 - 1 개로 범위 분할
    first, others = max_range.start, max_range[1:]

    # NOTE - step_over() 함수는 한 칸 이동하고 난 이후의 일을 처리하므로, 최초 지점은 직접 찍어야 한다.
    matrix[y][x] = Item(first)

    # 결국 n**2 - 1 번만 찍으면 된다.
    for index in others:

        # 이동 가능할 때 까지 쭉 직진하며 찍는다.
        while not step_over(matrix, index, position, direction):
            # 이동 불가능해지면 방향 전환 경로 탐색
            direction = get_next_direction(direction)

    print_matrix(matrix)


if __name__ == '__main__':
    solve(5, Direction.RIGHT)
    solve(4, Direction.BOTTOM)

    solve(5, Direction.RIGHT, False)
    solve(6, Direction.BOTTOM, False)

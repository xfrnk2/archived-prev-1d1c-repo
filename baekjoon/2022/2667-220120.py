# https://www.acmicpc.net/problem/2667
from collections import deque

N = int(input())
visited = set()
field = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def init():
    for _ in range(N):
        a = input()
        field.append(a)


def visit(a, b):
    queue = deque()
    queue.append((a, b))
    house_count = 0

    while queue:
        x, y = queue.popleft()
        if x < 0 or y < 0 or N <= x or N <= y:
            continue
        elif field[x][y] == '0' or (x, y) in visited:
            continue

        visited.add((x, y))
        house_count += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            queue.append((nx, ny))

    return house_count


def solution():
    areas = []
    init()
    for i in range(N):
        for j in range(N):
            result = visit(i, j)
            if 0 < result:
                areas.append(result)

    print(len(areas))
    for house_count in sorted(areas):
        print(house_count)

solution()

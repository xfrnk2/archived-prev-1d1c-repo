import copy
from itertools import product


def solution(key, lock):
    length = len(lock)
    final_length = length + (length - 1) * 2

    entire_field = [[0] * final_length for _ in range(final_length)]

    start_point = len(key) - 1
    for i in range(start_point, start_point + length):
        for j in range(start_point, start_point + length):
            entire_field[i][j] = lock[i - start_point][j - start_point]
    t = copy.deepcopy(entire_field)

    for c in range(4):
        for i, j in product(range(length + start_point), repeat=2):
            for m, n in product(range(len(key)), repeat=2):
                entire_field[m + i][n + j] = key[m][n] ^ entire_field[m + i][n + j]

            ans = []
            for x, y in product(range(len(lock)), repeat=2):
                ans.append(entire_field[x + start_point][y + start_point])
            if all(ans):
                return True

            entire_field = copy.deepcopy(t)

        # 회전하기(시계방향)
        new_key = []
        for i in range(len(key)):
            temp = []
            for j in range(len(key) - 1, -1, -1):
                temp.append(key[j][i])

            new_key.append(temp)
        key = new_key
    return False

print(solution(key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

print(solution(key = [[1, 1, 0], [1, 0, 0], [0, 0, 1]], lock=[[1, 0, 0, 1], [1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]]))



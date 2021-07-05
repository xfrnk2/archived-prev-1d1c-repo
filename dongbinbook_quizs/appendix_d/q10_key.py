# https://programmers.co.kr/learn/courses/30/lessons/60059
'''
실패하는 코드. 1차

'''


def solution(key, lock):
    turn_counts = 0
    while turn_counts < 3:
        current_key = []

        for i in range(3):
            row = []
            for j in range(2, -1, -1):
                row.append(_key[j][i])
            current_key.append(row)

        _key = current_key
        # print(current_key)
        turn_counts += 1

        keys = []
        for i in range(3):

            for j in range(3):
                temp = []
                for k in range(i):
                    temp.append(_key[k][j])
                temp.append(_key[i][j])
                keys.append(temp)

